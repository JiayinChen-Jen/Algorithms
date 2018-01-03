import numpy 
import numpy.random as rand

def build_heap(array, name='max'):
	"""Build a max heap from an unordered array."""
	n = heap_size(array)
	max_ind = int(n/2)  
	for key in reversed(range(0, max_ind)):
		if name == 'max': 
			new_heap = max_heapify(array, key)
		elif name == 'min':
			new_heap = min_heapify(array, key)
		array = new_heap
	return array 

def max_heapify(heap, key):
	"""Correct a SINGLE violation of the heap in a subtree at root."""
	leftInd = get_leftChild(key)
	rightInd = get_rightChild(key)
	if (leftInd <= heap_size(heap)-1) and (heap[leftInd] > heap[key]):
		largest_key = leftInd
	else:
		largest_key = key
	if (rightInd <= heap_size(heap)-1) and (heap[rightInd] > heap[largest_key]):
		largest_key = rightInd
	if largest_key != key:
		heap[key], heap[largest_key] = heap[largest_key], heap[key]
		max_heapify(heap, largest_key)
	return heap

def extract_max(heap):
	"""return largest key and remove."""
	heap.pop(0)
	return heap

def min_heapify(heap, key):
	"""Correct a SINGLE violation in the min heap."""
	leftInd = get_leftChild(key)
	rightInd = get_rightChild(key)
	if (leftInd <= heap_size(heap)-1) and (heap[leftInd] < heap[key]):
		smallest_key = leftInd
	else:
		smallest_key = key 
	if (rightInd <= heap_size(heap)-1) and (heap[rightInd] < heap[smallest_key]): 
		smallest_key = rightInd
	if smallest_key != key:
		heap[key], heap[smallest_key] = heap[smallest_key], heap[key]
		min_heapify(heap, smallest_key)
	return heap 

def heapSort(array, name='max'):
	"""Take nlog(n) time to sort."""
	sortedList = [ ]
	heap = build_heap(array, name)
	while heap_size(heap) > 0 :
		heap[0], heap[-1] = heap[-1], heap[0]
		sortedList.append(heap[-1])
		heap.pop(-1)
		if name == 'max':
			max_heapify(heap, 0)
		elif name == 'min':
			min_heapify(heap, 0)
	return sortedList

def heap_size(heap):
	return len(heap)

def get_parent(key):
	"""Index of parent."""
	if key%2 == 0:
		parent = int(key/2)-1
	else:
		parent = int(key/2)
	return parent

def get_leftChild(key):
	"""Index of left child."""
	return int(key*2+1)

def get_rightChild(key):
	"""Index of right child."""
	return int(key*2+2)


""" Testing """
# heap1 = [16, 4, 10, 14, 7, 9, 3, 2, 8 ,1]
# heap2 = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
# heap3 = [1, 5, 4, 2, 7, 11, 13, 3, 4]
# print(max_heapify(heap1, 1))
# print(build_heap(heap2, 'max'))
# array = rand.randint(100, size = 20).tolist()
# print(heapSort(array, name='min'))
# print(min_heapify(heap3, 1))
# print(build_heap(heap1, 'min'))