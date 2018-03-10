"""
Program to solve a given system of linear equations using Gaussian elimination with 'partial pivoting'.

"""

import numpy as np


def gauss_elim(A, X):
    # 1) Find the maximum element(pivot"p") in a given column from ith row
    for i in range(0, n):             # iteration over columns
        # p - maximum value and rmax - row index corresponding to the max value
        (p, rmax) = max([(value, index)
                         for index, value in enumerate(abs(A[i:, i]))])
        rmax = rmax + i               # the index returned above is relative to ith row

    # 2) Swap the ith row with the rmax row except if ith row already has the max element
        if i != rmax:
            A[i, :] = A[i, :] + A[rmax, :]
            A[rmax, :] = A[i, :] - A[rmax, :]
            A[i, :] = A[i, :] - A[rmax, :]

    # 3) Make all the entries below the pivot zero by transforming the rows  k-row number j-column number
        for k in range(i+1, n):              # iteration over rows below the pivoted row
            # A(k,i) is the first element in the kth row and the pivoted column | A[i][i] is the pivot
            m = -1.0*A[k][i]/A[i][i]
            # iteration over columns in the kth row to the right of ith column of the augmented matrix
            for j in range(i, n+1):
                if j == i:
                    A[k][j] = 0.0           # elements below the pivot
                else:
                    # kth row is added with the pivoted row times m
                    A[k][j] += m*A[i][j]
        print(A)
        print("")

    # 4) Back substitution
    for i in range(n-1, -1, -1):
        X[i] = 1.0*A[i][n]/A[i][i]
        for k in range(i-1, -1, -1):
            A[k][n] -= A[k][i]*X[i]

    return X



# Input the coefficient matrix (RHS values are not included in this matrix) - row by row, each coefficient separated by a whitespace
n = int(input("Enter the number of variables : "))

A = [[None]*n]*n
B = [None]*n
X = [None]*n
print("Enter the coefficient matrix, row by row, and each coefficents separated by a whitespace : ")

for i in range(0, n):
    try:
        A[i] = np.fromstring(input(), sep=' ', count=n)
    except ValueError:
        A[i] = np.fromstring(input(
            "Please enter exactly {:d} coefficients for {:d}th row again : ".format(n, i+1)), sep=' ', count=n)

# Input the RHS column vector
B = np.fromstring(input("Enter the RHS vector : "), sep=' ', count=n)

# Create Augmented matrix
for i in range(0, n):
    A[i] = np.append(A[i], B[i])

A = np.array(A)
print("")
print(A)
print("")

# Call the Gaussian elimination function on Augmented matrix A
X = gauss_elim(A, X)

# Print the solutions
print("The solutions of the given equations are : ")

for i in range(0, n):
    print("x{:d} = ".format(i+1), X[i])
