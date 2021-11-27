import operator

def is_sorted(r, key=operator.le):
	r_shifted = iter(r)
	next(r_shifted)
	return all(key(a, b) for a, b in zip(r, r_shifted))