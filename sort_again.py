"""Sorting algorithm implemented again..."""
"""Quick sort"""
import numpy as np
import numpy.random as rand
def quick_sort(array, start, p):
	if start < p:
		q = partition(array, start, p)
		quick_sort(array, start, q-1)
		quick_sort(array, q+1, p)
	return array

def partition(array, start, p):
	pivot = array[p]
	i = start - 1
	for j in range(start, p):
		if array[j] <= pivot:
			i += 1 
			array[i], array[j] = array[j], array[i]
	q = i + 1
	if array[start] == array[q] and q == p:
		q = int((start+p)/2)
	else:
		array[q], array[p] = array[p], array[q]
	return q

def quick_sort_nonincreasing(array, start, p):
	if start < p:
		q = nonincreasing_partition(array, start ,p)
		quick_sort_nonincreasing(array, start, q-1)
		quick_sort_nonincreasing(array, q+1, p)
	return array


def nonincreasing_partition(array, start, p):
	pivot = array[p]
	i = start - 1
	for j in range(start, p):
		if array[j] >= pivot:
			i += 1
			array[i], array[j] = array[j], array[i]
	q = i + 1
	array[q], array[p] = array[p], array[q]
	return q


def random_quickSort(array, start, p):
	if start < p:
		q = random_partition(array, start, p)
		random_quickSort(array, start, q-1)
		random_quickSort(array, q+1, p)
	return array

def random_partition(array, start, p):
	i = rand.randint(start, p)
	array[i], array[p] = array[p], array[i]
	return partition(array, start, p)


def Hoare_partition(array, p, r):
	pivot = array[p]
	i = p  
	j = r 
	while True:
		while array[j] > pivot:
			j -= 1
		while array[i] < pivot:
			i += 1
		if i < j:
			array[i], array[j] = array[j], array[i]
		else:
			return j

def Hoare_quickSort(array, p, r):
	if p < r:
		q = Hoare_partition(array, p, r)
		Hoare_quickSort(array, p, q - 1)
		Hoare_quickSort(array, q + 1, r)
	return array

def counting_sort(A, k):
	B = np.zeros(len(A)+1, dtype=int)
	C = np.zeros(k, dtype = int)
	for j in range(len(A)):
		C[A[j]] = C[A[j]] + 1
	for i in range(1, k):
		C[i] = C[i] + C[i-1]
	for j in reversed(range(len(A))):
		B[C[A[j]]] = A[j]
		C[A[j]] -= 1
	return B[1:]

def radix_sort(M, d, k):
	# d is the number of digit 
	# IMPORTANT: radix sort requires a stable sorter
	M_prime = np.zeros(M.shape, dtype=int)
	for i in reversed(range(d)):
		A = M[:,i]
		sorted_A = counting_sort(A, k)
		M_prime[:, i] = sorted_A
	return M_prime

def count_bins(A, k):
	B = np.zeros(k, dtype=int)
	for j in range(len(A)):
		B[A[j]] += 1
	for i in range(1, k):
		B[i] += B[i-1]
	return B

def query(A, k, R):
	max_value = R[-1]
	min_value = R[0]
	B = count_bins(A, k)
	total_number = B[max_value] - B[min_value-1]
	return total_number


array = rand.randint(5, size =10)
print(array)
# array = np.unique(array)
# array = [2,8,7,1,3,5,6,4]
print(query(array, 5, [2,3]))
matrix = rand.randint(5,size=(5,5))
print(radix_sort(matrix, 5, 5))
# print(counting_sort(array, 5))
# print(Hoare_quickSort(array, 0, len(array)-1))
# print(partition(array, 0, len(array)-1))
# print(nonincreasing_partition(array, 0 , len(array)-1))
# print(quick_sort(array, 0, len(array)-1))
# print(quick_sort_nonincreasing(array, 0, len(array)-1))
# print(random_partition(array, 0, len(array)-1))
# print(random_quickSort(array, 0, len(array)-1))