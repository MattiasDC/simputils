import operator

from .functional import identity

def is_sorted(iterable, key=identity):
	sentinel = object()
	iterable_shifted = iter(r)
	if next(iterable_shifted, sentinel) is sentinel:
		return True # empty iterable
	return all(key(a) <= key(b) for a, b in zip(iterable, iterable_shifted))

from itertools import groupby

def all_equal(iterable, key=identity):
    g = groupby(iterable, key)
    return next(g, True) and not next(g, False)