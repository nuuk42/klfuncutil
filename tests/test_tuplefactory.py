import logging
import pickle
from unittest import TestCase, main

from klfuncutil.tuplefactory import tuple_factory


class TestTupleFactory(TestCase):
    def test_same_name_returns_same_class(self):
        first = tuple_factory("person", name="Kalle", age=42)
        second = tuple_factory("person", age=42, name="Kalle")
        self.assertEqual(first, second)
        self.assertIs(type(first), type(second))

    def test_field_order_is_defined_by_first_call(self):
        tuple_factory("ordered_person", name="Kalle", age=42)
        second = tuple_factory("ordered_person", age=42, name="Kalle")
        self.assertEqual(second._fields, ("name", "age"))

    def test_different_fields_raise(self):
        tuple_factory("person_without_age", name="Kalle", age=42)
        with self.assertRaises(ValueError):
            tuple_factory("person_without_age", name="Kalle")

    def test_anonymous_classes_are_not_cached(self):
        first = tuple_factory(a=1, b=2)
        second = tuple_factory(a=1, b=2)
        self.assertEqual(first, second)
        self.assertIsNot(type(first), type(second))

    def test_name_can_be_used_as_field(self):
        record = tuple_factory("named_record", name="Kalle", age=42)
        self.assertEqual(record.name, "Kalle")

    def test_named_tuple_can_be_pickled(self):
        record = tuple_factory("pickled_person", name="Kalle", age=42)
        restored = pickle.loads(pickle.dumps(record))
        self.assertEqual(restored, record)
        self.assertIs(type(restored), type(record))

    def test_anonymous_tuple_can_be_pickled(self):
        record = tuple_factory(name="Kalle", age=42)
        restored = pickle.loads(pickle.dumps(record))
        self.assertEqual(restored, record)


if __name__ == "__main__":
    logging.basicConfig(filename="tests.log", level=logging.DEBUG)
    main()
