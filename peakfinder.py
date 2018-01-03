import numpy as np
import numpy.random as rand
import math


def peakfinder(array):
	peak = np.zeros(len(array))
	for ind in range(1,len(array)-1):
		if array[ind] >= array[ind-1] and array[ind] >= array[ind+1]: 
			peak[ind] = 1
	if array[0] >= array[1]:
		peak[0] = 1
	if array[-1] >= array[-2]:
		peak[-1] = 1
	return peak

def peakfinder2(array):
	while len(array) > 2:
		ind = int(math.floor(len(array)/2))
		if array[ind-1] > array[ind]:
			array = array[:ind]
		elif array[ind+1] > array[ind]:
			array = array[ind+1:]
		else:
			return array[ind]
	if len(array) == 1:
		peak = array[0]
	else:
		if array[0] >= array[1]:
			peak = array[0]
		else:
			peak = array[1]
	return peak

def peakfinder2D(array):
	if len(array) == 1:
		array = array[0]
		peak = peakfinder2(array)
		return peak

	while len(array[0])>2:
		col_ind = int(math.floor(len(array[0])/2))
		global_max, max_row = _gloabl_max(array, col_ind)
		if array[max_row][col_ind+1] > array[max_row][col_ind]:
			array = [sublist[col_ind+1:] for sublist in array]
		elif array[max_row][col_ind-1] > array[max_row][col_ind]:
			array = array[:][ :col_ind-1]
		else:
			return global_max

	if len(array[0]) == 2:
		col_ind = 0
		global_max, max_row = _gloabl_max(array, col_ind)
		if array[max_row][col_ind+1] > array[max_row][col_ind]:
			array = [sublist[col_ind+1:] for sublist in array]
		else:
			return global_max

	if len(array[0]) == 1:
		array = [sublist[0] for sublist in array]
		peak = peakfinder2(array)
	return peak 

def _gloabl_max(array, col_ind):
	global_max = -1
	for row_ind in range(len(array)):
		if array[row_ind][col_ind] > global_max:
			global_max = array[row_ind][col_ind]
			max_row = row_ind
	return global_max, max_row

# print(peakfinder2D([[1]]))
# print(peakfinder2D([[1,2,3,4],[1,2,3,4]]))
# print(peakfinder2D([[4,2,3,4,4], [1,2,3,4,2]])) 
array = rand.randint(28, size=(5,5)).tolist()
print(array)
print(peakfinder2D(array))
# print(array)
# print(peakfinder2(array))
# print(peakfinder2([1]))
# print(peakfinder2([1,2,3,4,5]))
# print(peakfinder2([5,4,3,2,1]))
# print(peakfinder2([1,2,3,2,1]))
