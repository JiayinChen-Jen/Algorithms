import numpy as np 
import numpy.random as rand
import math
from copy import deepcopy

def insertion_sort(array):
	"""Insertion sorting.
	pairwise key-swaps down to its right position."""
	n = len(array)
	for ind in range(1, n): 
		while (ind > 0) and (array[ind] < array[ind-1]):
			temp = array[ind-1]
			array[ind-1] = array[ind]
			array[ind] = temp 
			ind -=1
	return array

def reverse(array):
	reverse = [array[i] for i in reversed(range(len(array)))]
	return reverse	

def insertion_nonincreasing(array):
	"""Two ways: insert_sort then reverse the array or start at the end."""
	array_1 = insertion_sort(array)
	array_1 = reverse(array_1)

	n = len(array)
	for ind in reversed(range(0, n-1)):
		while (ind < n-1) and (array[ind] < array[ind+1]):
			temp = array[ind+1]
			array[ind+1] = array[ind]
			array[ind] = temp
			ind +=1
	return array_1, array	

def shift_up(array, start, end):
	for i in reversed(range(start+1, end)):
		array[i] = array[i-1]

def binary_sort(array):
	"""Binary insertion sorting.
	Use binary search to find the right position.""" 
	n = len(array)
	for ind in range(1, n):
		target = array[ind]
		position = binary_search(array[0:ind], target)
		shift_up(array, position+1, ind+1)
		array[position+1] = target
	return array

def binary_search(array, target):
	"""Find the position of the target within the sorted array."""
	# check if the array is sorted in ascending order
	L = 0 
	R = len(array) - 1 
	while (R - L >= 0):
		if array[L] > target: return L-1
		if array[R] < target: return R

		m = int(math.floor((L+R)/2))
		if array[m] == target:
			break
		elif array[m] > target:
			R = m - 1
		else:
			L = m + 1 

	return int(math.floor((L+R)/2))

def merge_sort(array):
	if len(array) > 1:
		m = int(len(array)/2)
		array1 = merge_sort(array[0:m])
		array2 = merge_sort(array[m:])
		array = merge(array1, array2)
	return array

def merge(array1, array2):
	ind1 = 0
	for ind2 in range(len(array2)):
		while array2[ind2] > array1[ind1]:
			ind1 += 1
			if ind1 >= len(array1):
				return array1 + array2[ind2:]
		array1.insert(ind1, array2[ind2])
	return array1

def quicksort(array):
	lesser = []
	greater = []
	if len(array) > 1:
		pivot = array[0]
		for ind in range(1, len(array)):
			ele = array[ind]
			if ele <= pivot:
				lesser.append(ele)
			else:
				greater.append(ele)
		lesser = quicksort(lesser)
		greater = quicksort(greater)
		array = lesser + [pivot] + greater 
	return array

def bubblesort(array):
	flag = True
	while flag:
		flag = False 
		for ind in range(len(array)-1):
			if array[ind] > array[ind+1]:
				array[ind], array[ind+1] = array[ind+1], array[ind]
				flag = True
	return array
			

# array = rand.randint(20, size=20).tolist()
# array2 = sorted(rand.randint(20, size=5).tolist())
# print(quicksort(array))
# print(bubblesort(array))
# print ('original:',array)
# print(insertion_nonincreasing(array))
# print(insertion_sort(array))
# print(binary_sort(array))

