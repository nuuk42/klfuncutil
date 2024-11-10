import logging
from unittest import TestCase, main
import itertools
from klfuncutil.collection import *


class TestIter(TestCase):
    def setUp(self):
        self.input, self.input_copy = itertools.tee(iter((1, 2, 3)), 2)
        self.result = None
        self.append_element = None
        self.append_collection = None
        self.input_id = id(self.input)

    def tearDown(self):
        # make sure the the input-iter contains the same elements as the result
        for x in self.input_copy:
            y = next(self.result)
            self.assertEqual(x, y)

        if self.append_element is not None:
            # make sure that the appended element is last in the iterator
            z = next(self.result)
            self.assertTrue(z == self.append_element)

        if self.append_collection is not None:
            for x in self.append_collection:
                y = next(self.result)
                self.assertEqual(x, y)

        # make sure that input ist unchanged
        self.assertEqual(self.input_id, id(self.input))
        # make sure to result contains a different object
        self.assertNotEqual(self.input_id, id(self.result))

    def test_append_number(self):
        self.result = append_element(self.input, 4)
        self.append_element = 4

    def test_append_string(self):
        self.result = append_element(self.input, "Kalle")
        self.append_element = "Kalle"

    def test_append_num_list(self):
        self.result = append_collection(self.input, [100, 200, 300])
        self.append_collection = [100, 200, 300]

    def test_append_str_list(self):
        self.result = append_collection(self.input, "Kalle")
        self.append_collection = ["K", "a", "l", "l", "e"]

    def test_append_num_iter(self):
        self.result = append_collection(
            self.input, filter(lambda x: x != 400, [100, 200, 300, 400])
        )
        self.append_collection = [100, 200, 300]

    def test_remove_element(self):
        self.result = append_element(self.input, 4)
        self.append_element = 4
        i1 = iter([1, 2, 3])
        i2 = remove_element(i1, 2)
        l2 = list(i2)
        self.assertEqual(l2, [1, 3])


if __name__ == "__main__":
    logging.basicConfig(filename="tests.log", level=logging.DEBUG)
    main()
