import numpy as np


def swap_rows(A, i, j):
    if i == j:
        return A
    else:
        A[i, :] = A[i, :] + A[j, :]
        A[j, :] = A[i, :] - A[j, :]
        A[i, :] = A[i, :] - A[j, :]
        return A


def pivot(M):

    P = np.identity(M.shape[0])
    n = M.shape[0]

    for i in range(0, n):             # iteration over rows
        # p - maximum value and rmax - row index corresponding to the max value
        (p, rmax) = max([(value, index)
                         for index, value in enumerate(abs(M[i:, i]))])
        rmax = rmax + i               # the index returned above is relative to ith row

    # Swap the ith row with the rmax row except if ith row already has the max element
        if i != rmax:
            A = swap_rows(M, i, rmax)
            P = swap_rows(P, i, rmax)
    return P


def LU_decomp(A):
    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, A.shape[1]))

    P = pivot(A)
    A = np.matmul(P, A)

    # Dolittle algorithm
    for k in range(n):
        L[k][k] = 1.0
        for m in range(k, A.shape[1]):
            s1 = sum(U[j][m] * L[k][j] for j in range(k))
            U[k][m] = A[k][m] - s1
        for i in range(k+1, n):
            s2 = sum(U[j][k] * L[i][j] for j in range(k))
            L[i][k] = (A[i][k] - s2) / U[k][k]
    return L, U, P


n = 100
b = 10

if n > b:
    n = n + b
    b = n - b
    n = n - b

A = np.zeros((n, b))

for i in range(0, n):
    for j in range(0, b):
        A[i][j] = 1.0/(i+j+1)

print(A)

A = np.array(A)
L, U, P = LU_decomp(A)

print("L:")
print(L)
print("U:")
print(U)
print("P")
print(P)
print(np.matmul(L, U))
print("Diff")

print(np.subtract(np.matmul(L, U), np.matmul(P, A)))
