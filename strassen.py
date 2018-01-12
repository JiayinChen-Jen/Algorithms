"""Matrix multiplication"""
import numpy as np
import numpy.random as rand
from functools import reduce

def matrix_multiplication(A, B):
	"""Compute matrix multiplication with A (nxm), B (mxp)"""
	n = A.shape[0]
	p = B.shape[1]
	C = np.zeros((n, p))
	for r in range(n):
		for c in range(p):
			C[r,c] = np.sum(np.multiply(A[r,:], B[:,c]))
	return C

def square_divide_conquer(A, B):
	"""Assume square matrices with n is a power of 2."""
	n = A.shape[0]
	C = np.zeros((n, n))
	if n == 1:
		C[0,0] = A[0,0] * B[0,0]
	else:
		ind = int(n / 2)
		C[0:ind, 0:ind] = square_divide_conquer(A[0:ind,0:ind], B[0:ind, 0:ind]) + square_divide_conquer(A[0:ind:,ind:], B[ind:, 0:ind])
		C[0:ind, ind:] = square_divide_conquer(A[0:ind,0:ind], B[0:ind, ind:]) + square_divide_conquer(A[0:ind, ind:], B[ind:, ind:])
		C[ind:, 0:ind] =  square_divide_conquer(A[ind:,0:ind], B[0:ind, 0:ind]) + square_divide_conquer(A[ind:, ind:], B[ind:, 0:ind])
		C[ind:, ind:] = square_divide_conquer(A[ind:,0:ind], B[0:ind, ind:]) + square_divide_conquer(A[ind:, ind:], B[ind:, ind:])
	return C

def strassen_method(A, B):
	"""Assume square matrices with n a power of 2"""
	n = A.shape[0]
	C = np.zeros((n, n))
	if n == 1:
		C[0,0] = A[0,0] * B[0, 0]
	else: 
		ind = int(n / 2)
		A11, B11 = A[0:ind, 0:ind], B[0:ind, 0:ind]
		A12, B12 = A[0:ind, ind:], B[0:ind, ind:]
		A21, B21 = A[ind:, 0:ind], B[ind:, 0:ind]
		A22, B22 = A[ind:, ind:], B[ind:, ind:]
		S1 = np.subtract(B12, B22)
		S2 = np.add(A11 , A12)
		S3 = np.add(A21 , A22)
		S4 = np.subtract(B21 , B11)
		S5 = np.add(A11, A22)
		S6 = np.add(B11, B22)
		S7 = np.subtract(A12, A22)
		S8 = np.add(B21, B22)
		S9 = np.subtract(A11, A21)
		S10 = np.add(B11, B12)
		P1 = strassen_method(A11, S1)
		P2 = strassen_method(S2, B22)
		P3 = strassen_method(S3, B11)
		P4 = strassen_method(A22, S4)
		P5 = strassen_method(S5, S6)
		P6 = strassen_method(S7, S8)
		P7 = strassen_method(S9, S10)
		C[0:ind, 0:ind] = np.subtract(reduce(np.add, [P5, P4, P6]), P2)
		C[0:ind, ind:] = np.add(P1, P2)
		C[ind:, 0:ind] = np.add(P3, P4)
		C[ind:, ind:] = reduce(np.subtract, [np.add(P5, P1), P3, P7])
	return C 


def main():
	A = rand.randint(15, size=(8, 8))
	B = rand.randint(15, size=(8, 8))
	C = matrix_multiplication(A, B)
	C_prime = square_divide_conquer(A, B)
	C_strassen = strassen_method(A, B)
	print(np.equal(C, C_strassen))

if __name__ == '__main__':
	main()