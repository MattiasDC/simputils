import math


def sign(value):
    if value == 0:
        return abs(value)
    return math.copysign(1, value)


def is_equal(value, other, epsilon=1e-9):
    return abs(value - other) < epsilon


def is_zero(value, epsilon=1e-9):
    return is_equal(value, 0, epsilon)
