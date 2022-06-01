from collections import defaultdict
from itertools import chain, filterfalse, groupby, zip_longest

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


def split_elements(iterable, key=identity):
    """
    Return an iterable of lists.
    Each list contains elements which are considered equal according to the key.
    This algorithms can be used to split elements which are not sortable"""
    mappings = defaultdict(list)
    for e in iterable:
        mappings[key(e)].append(e)
    return flatten(mappings.values())


def max_dist_indices_impl(low, high):
    if abs(low - high) <= 1:
        yield low
        if low != high:
            yield high
        return

    split_point = (low + high) // 2
    yield split_point
    lower_dist = (split_point - 1) - low
    upper_dist = high - (split_point + 1)
    lower_half = max_dist_indices_impl(low, split_point - 1)
    upper_half = max_dist_indices_impl(split_point + 1, high)

    if lower_dist > upper_dist:
        yield from filterfalse(
            lambda x: x is None, chain(*zip_longest(lower_half, upper_half))
        )
        return
    yield from filterfalse(
        lambda x: x is None, chain(*zip_longest(upper_half, lower_half))
    )


def max_dist_indices(n):
    """Generates a sequence of indices up to `n`.
    The indices are sequenced to be as distant as possible
    from any other previously generated index.
    """
    if n == 0:
        return
    if n == 1:
        yield 0
        return

    yield 0
    yield n - 1
    yield from max_dist_indices_impl(1, n - 2)
