"""Implement a d_heap where each non-leaf node has d children"""
import numpy as np
import numpy.random as rand
from graphviz import Digraph

def max_heapify(heap, key, d):
	largest_key = key
	for j in range(1,d+1):
		if (key * d + j < len(heap)) and (heap[key * d + j] > heap[largest_key]):
			largest_key = key * d + j
	if largest_key != key:
		heap[largest_key], heap[key] = heap[key], heap[largest_key]
		heap = max_heapify(heap, largest_key, d)
	return heap

def build_heap(array, d):
	n = len(array)
	max_ind = int(n/(d-1))
	for key in reversed(range(max_ind)):
		new_heap = max_heapify(array, key, d)
		array = new_heap
	return array

def extract_max(heap, d):
	Max = heap[0]
	heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
	heap.pop(-1)
	heap = max_heapify(heap, 0, d)
	return Max, heap

def increase_val(heap, d, key, val):
	if heap[key] > val:
		raise ValueError('new key smaller than original key')
	heap[key] = val
	parentInd = get_parent(key, d)
	while key > 0 and heap[parentInd] < val:
		heap[parentInd], heap[key] = heap[key], heap[parentInd]
		key = parentInd
		parentInd = get_parent(key)
	return heap

def insert(heap, d, key, val):
	heap.append(-10e8)
	heap = increase_val(heap, d, len(heap)-1, val)
	return heap

def get_j_child(key, j, d):
	if j > d:
		raise ValueError('only {} children'.format(d))
	return key * d + j

def get_parent(key, d):
	return int((key-1)/d)

def show_heap(heap, d):
	dot = Digraph(comment='Maximum heap')
	dot.node(str(0), str(heap[0]))
	for ind in range(1, len(heap)):
		parentInd = get_parent(ind, d)
		print(parentInd)
		dot.node(str(ind), str(heap[ind]))
		dot.edge(str(parentInd), str(ind))
	dot.render('max_d_heap.gv', view=True)

"""Testing"""
array = rand.randint(10, size = 10)
heap = build_heap(array, 2)
show_heap(heap, 2)