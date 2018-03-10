import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library
import numpy as np

n = 100
b = 6

A = np.zeros((n, b))

for i in range(n):
    for j in range(b):
        A[i][j] = 1.0/(i+j+1)

print("A:")
pprint.pprint(A)

P, L, U = scipy.linalg.lu(A)


print("P:")
pprint.pprint(P)

print("L:")
pprint.pprint(L)

print("U:")
pprint.pprint(U)

print(np.matmul(L, U))
print(np.subtract(np.matmul(L, U), np.matmul(P, A)))
