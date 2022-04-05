from collections import defaultdict
from itertools import groupby

from more_itertools import flatten

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


"""
Return an iterable of lists.
Each list contains elements which are considered equal according to the key.
This algorithms can be used to split elements which are not sortable
"""


def split_elements(iterable, key=identity):
    mappings = defaultdict(list)
    for e in iterable:
        mappings[key(e)].append(e)
    return flatten(mappings.values())
