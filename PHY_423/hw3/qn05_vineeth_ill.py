import numpy as np


def swap_rows(A, i, j):
    if i == j:
        return A
    else:
        A[i, :] = A[i, :] + A[j, :]
        A[j, :] = A[i, :] - A[j, :]
        A[i, :] = A[i, :] - A[j, :]
        return A


def LU_decomp(A, n):
    # P is the permutation matrix whose rows are swapped in the same manner as A
    P = np.identity(A.shape[0])

    L = np.identity(A.shape[0])

    # 1) Find the maximum element(pivot"p") in a given column from ith row
    for i in range(0, n):             # iteration over columns
        # p - maximum value and rmax - row index corresponding to the max value
        (p, rmax) = max([(value, index)
                         for index, value in enumerate(abs(A[i:, i]))])
        rmax = rmax + i               # the index returned above is relative to ith row

    # 2) Swap the ith row with the rmax row except if ith row already has the max element
        if i != rmax:
            A = swap_rows(A, i, rmax)
            P = swap_rows(P, i, rmax)

    # 3) Make all the entries below the pivot zero by transforming the rows  k-row number j-column number
        for k in range(i+1, n):              # iteration over rows below the pivoted row
            # A(k,i) is the first element in the kth row and the pivoted column | A[i][i] is the pivot
            m = -1.0*A[k][i]/A[i][i]
            L[k][i] = -1.0*m

            # iteration over columns in the kth row to the right of ith column of the augmented matrix
            for j in range(i, n):
                if j == i:
                    A[k][j] = 0.0           # elements below the pivot
                else:
                    # kth row is added with the pivoted row times m
                    A[k][j] += m*A[i][j]
    return L, A, P


n = 10
b = 10

A = [[None]*n]*b

for i in range(0, n):
    for j in range(0, b):
        A[i][j] = 1.0/(i+j+1)

A = np.array(A)
L, U, P = LU_decomp(A, n)

print("")
print(L)
print("")
print(U)
print("")
print(P)
print("")
