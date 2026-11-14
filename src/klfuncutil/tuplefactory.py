"""Factory for cached named tuples.

The factory creates instances of ``collections.namedtuple``. Classes are
cached by name, so repeated calls with the same name use the same class.
"""

from collections import namedtuple

_classes = {}


def _restore_tuple(name, fields, values):
    """Rebuild a tuple created by ``tuple_factory`` during unpickling."""
    return tuple_factory(name, **dict(zip(fields, values)))


def _make_reduce(name, fields):
    """Create a ``__reduce__`` method for a generated tuple class."""

    def _reduce(self):
        return (_restore_tuple, (name, fields, tuple(self)))

    return _reduce


def tuple_factory(name="_", /, **kwargs):
    """Create a named tuple instance.

    The keyword arguments define the fields of the tuple. If ``name`` is
    not ``"_"``, the class is cached and reused for later calls with the
    same name. The field order is defined by the first call; later calls
    may pass the same fields in any order.

    ``name`` is positional-only, so ``name`` can also be used as a field
    name.

    Parameters:
    name : name of the generated class; ``"_"`` creates an uncached,
        anonymous class
    **kwargs : field names and values

    Return:
    an instance of the generated named tuple class

    Raises:
    ValueError : if a class with the same name but different fields
        already exists
    """
    fields = tuple(kwargs)

    # Anonymous classes are created for each call and are not cached.
    if name == "_":
        target_class = namedtuple(name, fields)
        target_class.__reduce__ = _make_reduce(name, fields)
        return target_class(**kwargs)

    target_class = _classes.get(name)

    if target_class is None:
        target_class = namedtuple(name, fields)
        target_class.__reduce__ = _make_reduce(name, fields)
        _classes[name] = target_class
    elif set(target_class._fields) != set(fields):
        raise ValueError(
            f"Klasse {name!r} existiert bereits mit den Feldern "
            f"{target_class._fields}, angefordert: {fields}"
        )

    return target_class(**kwargs)


if __name__ == "__main__":
    d1 = tuple_factory("kalle", a=1, b=2, c="x")
    d2 = tuple_factory("kalle", c="x", a=1, b=2)
    anonymous = tuple_factory(a=1, b=2)

    assert d1 == d2
    assert type(d1) is type(d2)
    assert anonymous.a == 1

    print(d1)
    print(anonymous)
