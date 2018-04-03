#!/usr/bin/env python3
"""
Program to find root of a function using bisection method
"""
import sys
import math
import numpy as np


def is_equal(a, b):
    return abs(b-a) < sys.float_info.epsilon


def bisection(f, a, b, TOL=0.001, MAX_ITER=100):
    f_a = f(a)
    f_b = f(b)
    iter = 0
    while iter < MAX_ITER:
        c = (a+b)/2
        f_c = f(c)
        if math.isclose(f_c, 0.0, abs_tol=1.0E-6) or abs(b-a)/2 < TOL:
            return (c, iter)
        else:
            if f_a * f_c < 0:
                b = c
                f_b = f_c
            else:
                a = c
                f_a = f_c
        iter = iter + 1


def func1(x):
    return x*x*x*x*x + x - 1.0


def func2(x):
    return np.sin(x) - 6*x - 5


def func3(x):
    return np.log(x) + x*x - 3


root1, iter = bisection(func1, 0, 1, TOL=1.0E-8, MAX_ITER=1000000)
root2, iter = bisection(func2, -1*np.pi/2, 0, TOL=1.0E-8, MAX_ITER=1000000)
root3, iter = bisection(func3, 1, np.e, TOL=1.0E-8, MAX_ITER=10000000)


print("root = {:10.8f}".format(root1), ", func1(x) = ", func1(root1))
print("root = {:10.8f}".format(root2), ", func2(x) = ", func2(root2))
print("root = {:10.8f}".format(root3), ", func3(x) = ", func3(root3))
