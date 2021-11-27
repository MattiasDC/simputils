import operator

from .functional import identity

def is_sorted(r, key=identity):
	r_shifted = iter(r)
	next(r_shifted)
	return all(key(a) <= key(b) for a, b in zip(r, r_shifted))