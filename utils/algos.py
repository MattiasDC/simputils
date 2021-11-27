import operator

from .functional import identity

def is_sorted(r, key=identity):
	sentinel = object()
	r_shifted = iter(r)
	if next(r_shifted, sentinel) is sentinel:
		return True # empty iterable
	return all(key(a) <= key(b) for a, b in zip(r, r_shifted))