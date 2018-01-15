"""Young tableas"""
import numpy as np

def extract_min(table):
	Min = table[0,0]
	table[0,0] = 10e9
	table = youngify(table, 0, 0)	
	return Min, table

def youngify(table, i, j):
	smallest_i = i
	smallest_j = j
	if i+1 < table.shape[0] and table[i+1, j] < table[i, j]:
		smallest_i = i+1
		smallest_j = j
	if j+1 < table.shape[1] and table[i, j+1] < table[smallest_i, smallest_j]:
		smallest_i = i
		smallest_j = j+1
	if smallest_i != i or smallest_j != j:
		table[i,j], table[smallest_i, smallest_j] = table[smallest_i, smallest_j], table[i,j]
		youngify(table, smallest_i, smallest_j)
	return table

def decrease(table, i, j, val):
	if table[i, j] < val:
		raise ValueError
	table[i, j] = val
	threshold = 10e9
	largest_i = i
	largest_j = j
	if i - 1 >= 0 and table[i, j] <= table[i-1, j]:
		largest_i = i-1
		largest_j = j
	if j - 1 >= 0 and table[largest_i, j] <= table[i, j-1]:
		largest_i = i
		largest_j = j-1
	if largest_i != i or largest_j != j:
		table[i, j], table[largest_i, largest_j] = table[largest_i, largest_j], table[i, j]
		decrease(table, largest_i, largest_j, val)
	return table 

def insert(table, val):
	table = decrease(table, len(table)-1, len(table)-1, val)
	return table 

def sort(array, table):
	sorted_array = []
	for elem in array:
		insert(table, elem)
	for _ in range(len(array)):
		Min, table = extract_min(table)
		sorted_array.append(Min)
	return sorted_array


"""Testing"""
table = [[2, 4, 9, 10e9], [3, 8, 16, 10e9], [5, 14, 10e9, 10e9], [12, 10e9, 10e9, 10e9]]
table = np.array(table)
print(insert(table, 1))
empty_table = np.zeros((4,4))
empty_table[:,:] = 10e9
array = np.random.randint(10, size=10)
print(sort(array, empty_table))