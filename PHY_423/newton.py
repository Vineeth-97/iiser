#!/usr/bin/env python3.5
"""
Modified Newton-Raphson method to find function root
"""
import sys
import math
import scipy.optimize

def is_equal(a, b):
	"""
	Check if floats `a' and `b' are equal within the machine precision
	"""
	return abs(a-b) < sys.float_info.epsilon

def newton(f, f_prime, a, TOL=1.0E-8, max_iter=100):
	"""
	f is the cost function, f_prime is first derivative, 
	a is the initital guess. TOL is tolerance.
	`max_iter' is the maximum number of iterartion.
	"""
	x = a
	f_x = f(x)
	iter = 0
	while (iter < max_iter):
		step_size = -f_x/f_prime(x)
		while abs(f_x) < abs(f(x+step_size)):
			step_size = step_size/2

		x = x + step_size
		f_x = f(x)
		if is_equal(f_x, 0.0) or abs(step_size)<TOL:
		#if math.isclose(f_x, 0.0, abs_tol=1.0E-6):
			return (x, iter) 
		iter = iter + 1
	return False

def func(x):
	"""
	f(x) = cos(x) - x	
	"""
	return math.cos(x) - x

def func_prime(x):
	"""
	f'(x) = -sin(x) - 1	
	"""
	return -math.sin(x) - 1.0

# the root
root, iter = newton(func, func_prime, 0.0)

print("Iterartion = ", iter)
print("root = ", root, ",func = ", func(root))


"""
Using the newton method from scipy
"""
root = scipy.optimize.newton(func, 0, fprime=func_prime)
print("scipy root = ", root, ",func = ", func(root))







