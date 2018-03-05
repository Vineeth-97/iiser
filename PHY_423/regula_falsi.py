#!/usr/bin/env python3.5

"""
Regula false method to find function root
"""
import sys
import math


def is_equal(a, b):
    """
    Check if floats `a' and `b' are equal within the machine precision
    """
    return abs(a-b) < sys.float_info.epsilon


def regula_fasi(f, a, b, TOL=0.001, max_iter=100):
    """
    The regula falsi algorithm for finding root
    f is the cost function, [a, b] is the initital bracket. 
    TOL is tolerance (default 0.001).
    `max_iter' is the maximum number of iterartion.
    """

    f_a = f(a)
    f_b = f(b)

    iter = 0
    while (iter < max_iter):
        c = (a * f_b - b * f_a)/(f_b - f_a)
        f_c = f(c)
        if is_equal(f_c, 0.0) or (b-a)/2.0 < TOL:
            # if math.isclose(f_c, 0.0, abs_tol=1.0E-6) or (b-a)/2.0<TOL:
            return (c, iter)
        else:
            if f_a * f_c < 0:
                b = c
                f_b = f_c
                f_a = f_a/2.0
            else:
                a = c
                f_a = f_c
                f_b = f_b/2.0
            iter = iter + 1
    return False


def func(x):
    """
    f(x) = cos(x) - x
    """
    return math.cos(x) - x


# the root
root, iter = regula_fasi(func, 0, 2)

print("Iterartion = ", iter)
print("root = ", root, ",func = ", func(root))
