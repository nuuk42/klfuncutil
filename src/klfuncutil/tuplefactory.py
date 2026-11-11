from collections import namedtuple

_classes = {}


def tuple_factory(name="_", /, **kwargs):
    fields = tuple(kwargs)

    # Anonyme Klassen bewusst nicht cachen.
    if name == "_":
        return namedtuple(name, fields)(**kwargs)

    target_class = _classes.get(name)

    if target_class is None:
        target_class = namedtuple(name, fields)
        _classes[name] = target_class
    elif set(target_class._fields) != set(fields):
        raise ValueError(
            f"Klasse {name!r} existiert bereits mit den Feldern "
            f"{target_class._fields}, angefordert: {fields}"
        )

    return target_class(**kwargs)

d1 = tuple_factory('kalle',a=1,b=2,c='x')
d2 = tuple_factory('kalle',c='x',a=1,b=2)
print(d1)
print(d2)
d3 = tuple_factory(a=1,b=2,y='x',p=9)
d4 = tuple_factory(e=1,ww=13)
print(d1.a)
print(d1.b)
print(d1.c)
print(dir(d2))
print(f'd2.__class__ = {d2.__class__}')
print(f'd1.__class__ = {d1.__class__}')
print(type(d2))
print(type(d2)==type(d1))
if isinstance(d1,d2.__class__):
    print('true')
else:
    print('false')
print ( d1 + d2 )
