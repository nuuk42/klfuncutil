from functools import wraps
def restartable(iter_returing_function):
    """Annoation to create re-startable iterators

    The annotation wraps a funktion that returns
    an iterator.
    The new function will return an object
    instead of an iterator. The object implemnts
    the "iterator" interfact in such a way the
    iterator can be execute multible times.

    Example:

    def get_some_iter1():
        return iter([1, 2, 3])

    i1 = get_some_iter1()
    assert list(i1) == [1, 2, 3]
    assert list(i1) == []

    @klfuncutil.iterator.restartable
    def get_some_iter2():
        return iter([4, 5, 6])

    i2 = get_some_iter2()
    assert list(i2) == [4, 5, 6]
    assert list(i2) == [4, 5, 6]

    Parameters:
    iter_returing_function : a function that returns an iterator

    Return:
    A new function that returns the iterator wrapped into a object
    """

    @wraps(iter_returing_function)
    def _wrapper(*args, **kwargs):
        class _Iter_Wrapper:
            def __init__(self, iter_fkt):
                self.iter_fkt = iter_fkt

            def __iter__(self):
                return self.iter_fkt(*args, **kwargs)

        iter_obj = _Iter_Wrapper(iter_returing_function)
        return iter_obj

    return _wrapper

