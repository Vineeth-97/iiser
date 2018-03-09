#!/usr/bin/env python3
"""
Program to find root of a function using bisection method
"""
import sys
import math

def is_equal(a,b):
	return abs(b-a) < sys.float_info.epsilon

def bisection(f,a,b,TOL=0.001,MAX_ITER=100):
	"""
	f is the cost function, [a,b] is the initial bracket, 
	TOL is tolerance, MAX_ITER is maximum iteration.
	"""
	f_a = f(a)
	f_b = f(b)

	iter = 0
	while iter < MAX_ITER:
		c = (a+b)/2
		f_c = f(c)

		#if is_equal(f_c, 0.0) or abs(b-a)/2<TOL:
		if math.isclose(f_c,0.0,abs_tol=1.0E-6) or abs(b-a)/2<TOL:
			return (c, iter)
		else:
			if f_a * f_c < 0:
				b = c
				f_b = f_c
			else:
				a = c
				f_a = f_c
			iter = iter + 1
	return None

def func(x):
	"""
	The cost function: f(x) = x^3 - 2x^2 + 4x/3 - 8/27
	"""
	return x*x*x - 2*x*x + 4.0*x/3 - 8.0/27.0

root, iter = bisection(func, 0, 1, TOL=1.0E-12)

print("Iteration = ", iter)
print("root = ", root, ", func(x) = ", func(root))



