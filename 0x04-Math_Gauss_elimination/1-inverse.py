#!/usr/bin/env python

import numpy as np
gauss_elim = __import__('0-gaussian_elimination').gaus_elim

if __name__ == "__main__":

    def inverse(A):
        B = np.zeros(np.shape(A))
        row, col = np.shape(B)

        i = 0
        for i in range(0, col):
            B[i][i] = 1

        A1 = gauss_elim(A, B)

        return A1

    A = np.zeros((4, 4))
    A[2, 0] = 1
    A[0, 1] = 1
    A[1, 3] = 1
    A[3, 2] = 1
    print("The matrix A:\n", A)
    print("The inverse of the matrix A:\n", inverse(A))
    menseje = "The identity matrix "
    menseje2 = "(The matrix A x The inverse of the matrix A):"
    print(f"{menseje}{menseje2} \n", A @ inverse(A))
