from itertools import izip as zip

def is_sorted(l):
	return all(a <= b for a, b in zip(l, l[1:]))