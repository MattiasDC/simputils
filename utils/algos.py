from itertools import groupby

from .functional import identity


def is_sorted(iterable, key=identity):
    sentinel = object()
    iterable_shifted = iter(iterable)
    if next(iterable_shifted, sentinel) is sentinel:
        return True  # empty iterable
    return all(key(a) <= key(b) for a, b in zip(iterable, iterable_shifted))


def all_equal(iterable, key=identity):
    g = groupby(iterable, key)
    return next(g, True) and not next(g, False)
