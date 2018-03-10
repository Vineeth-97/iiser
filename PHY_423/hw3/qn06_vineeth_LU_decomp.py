"""
Program to solve a given system of linear equations using LU decomposition

"""

import numpy as np

# swaps the ith and jth rows of A


def swap_rows(A, i, j):
    if i == j:
        return A
    else:
        A[i, :] = A[i, :] + A[j, :]
        A[j, :] = A[i, :] - A[j, :]
        A[i, :] = A[i, :] - A[j, :]
        return A

# Back substitution - A is the augmented matrix and X is the variable array


def back_sub(A, X):
    n = A.shape[0]
    if n != (A.shape[1] - 1):
        raise Exception('Cannot solve the given system of equations')
    else:
        for i in range(n-1, -1, -1):
            X[i] = 1.0*A[i][n]/A[i][i]
            for k in range(i-1, -1, -1):
                A[k][n] -= A[k][i]*X[i]
        return X

# Forward substitution - A is the augmented matrix


def forward_sub(A, X):
    n = A.shape[0]
    if n != (A.shape[1] - 1):
        raise Exception('Cannot solve the given system of equations')
    else:
        for i in range(0, A.shape[0]):
            X[i] = 1.0*A[i][n]/A[i][i]
            for k in range(i+1, n):
                A[k][n] -= A[k][i]*X[i]
        return X


def LU_decomp(A, n):
    # P is the permutation matrix whose rows are swapped in the same manner as A
    if A.shape[0] == A.shape[1]:
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


# Input the coefficient matrix (RHS values are not included in this matrix) - row by row, each coefficient separated by a whitespace
n = int(input("Enter the number of variables : "))

A = [[None]*n]*n
B = [None]*n
X = [None]*n
Y = [None]*n

print("Enter the coefficient matrix, row by row, and each coefficents separated by a whitespace : ")

for i in range(0, n):
    try:
        A[i] = np.fromstring(input(), sep=' ', count=n)
    except ValueError:
        A[i] = np.fromstring(input(
            "Please enter exactly {:d} coefficients for {:d}th row again : ".format(n, i+1)), sep=' ', count=n)

# Input the RHS column vector
B = np.fromstring(input("Enter the RHS vector : "), sep=' ', count=n)

A = np.array(A)
B = np.array(B)


#  LU decomposition of matrix A => LUx = PB

L, U, P = LU_decomp(A, n)
B = P.dot(B)

print("")
print(L)
print("")
print(U)
print("")
print(B)
print("")


# Solve for X
L = np.c_[L, B]
Y = forward_sub(L, Y)

U = np.c_[U, Y]
X = back_sub(U, X)

# Print the solutions
print("The solutions of the given equations are : ")

for i in range(0, n):
    print("x{:d} = ".format(i+1), X[i])
