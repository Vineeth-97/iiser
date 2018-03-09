#!/usr/bin/env python3
"""
Naive Gaussian Elimination to solve system of linear equations.
"""
import numpy as np

def GaussianElimination(A, b):
	"""
	A is n x n coefficient matrix
	b is n x 1 right-hand-side vector
	"""
	# matrix dimension
	n = len(b)
	if A.shape != (n,n):
		print('error: incorrect array sizes')
		return None

	# Elimination steps
	# for column j
	for j in range(n):
		pivot = A[j,j]
		if np.isclose(pivot,0.0,atol=1.0E-12):
			print('error: zero pivot encountered')
			return None
		# row below the main diagonal
		for i in range(j+1,n):
			ratio = A[i,j]/pivot
			# Coefficient matrix
			for k in range(j,n):
				A[i,k] = A[i,k] - A[j,k] * ratio
			# right-hand-side
			b[i] = b[i] - b[j]*ratio

	# Solutions by 'Back Substitution'
	x = b
	for i in range(n-1,-1,-1):
		for j in range(i+1,n):
			x[i] = x[i] - A[i,j] * x[j]
		x[i] = x[i]/A[i,i]
	return x

# define a test system of equations
A = np.array([(1,2,-1),(2,1,-2),(-3,1,1)])
b = np.array([3,3,-6])

sols = GaussianElimination(A, b)

print("Solution = ", sols)



