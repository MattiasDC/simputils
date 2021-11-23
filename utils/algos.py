from itertools import izip as zip

def is_sorted(r):
	r_shifted = iter(r)
	next(r_shifted)
	return all(a <= b for a, b in zip(r, r_shifted))