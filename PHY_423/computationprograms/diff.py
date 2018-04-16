import math
import numpy as np

def func(x):
	return 1/x

def func_prime(x):
	return -1/pow(x,2)

def func_2_prime(x):
	return 2/pow(x,3)

def func_3_prime(x):
	return -6/pow(x,4)

a=2.0
h=0.1
"""
def diff_first_order(f,func_2_prime,func_prime,a,h):
	f_prime_1=(f(a+h)-f(a))/h
	error_1=h*h*func_2_prime(a)/2
	exact_error=func_prime(a)-f_prime_1
	return f_prime_1,error_1,exact_error
"""

def diff_second_order(f,func_3_prime,func_prime,a,h):
	f_prime_2=(f(a+h)-f(a-h))/(2*h)
	error_2=-h*h*func_3_prime(a)/6
	exact_error=func_prime(a)-f_prime_2
	return f_prime_2,error_2,exact_error

"""

sol,error_1,exact_error=diff_first_order(func,func_2_prime,func_prime,a,h)
print("Soln = ",sol)
print("Evaluated error = ",error_1)
print("Exact error = ",exact_error)
"""

sol,error_2,exact_error=diff_second_order(func,func_3_prime,func_prime,a,h)
print("Soln = ",sol)
print("Evaluated error = ",error_2)
print("Exact error = ",exact_error)
