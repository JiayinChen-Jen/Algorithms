"""BST, all left nodes have KEY smaller than the right nodes."""
class BST(object):
	"""A node is defined as a dictionary of
	{'val': val, 'P': index of parent, 'L': index of left child, 'R': index of right child}"""
	def __init__(self, tree=[]):
		self.tree = tree

	def createNode(self, val):
		self.tree.append({'val': val, 'P': None ,'L': None, 'R': None, 'D': None})

	def insert(self, val):
		"""Wrapper for inserNode(). Handle root."""
		if len(self.tree) < 1:
			self.createNode(val)
		else:
			self._insertNode(0, val)

	def _insertNode(self, currentNodeidx, val):
		"""Insert a non root node."""
		currentNode = self.tree[currentNodeidx]
		if val <= currentNode['val']:
			leftChild = currentNode['L']
			if leftChild == None:
				self.createNode(val)
				self.tree[-1]['P'] = currentNodeidx
				currentNode['L'] = len(self.tree)-1
			else:
				self._insertNode(leftChild, val)
		elif val > currentNode['val']:
			rightChild = currentNode['R']
			if rightChild == None:
				self.createNode(val)
				self.tree[-1]['P'] = currentNodeidx
				currentNode['R'] = len(self.tree)-1
			else:
				self._insertNode(rightChild, val)

	def find(self, val):
		"""Wrapper for findNode() recursion."""
		return self._findNode(0, val)

	def _findNode(self, currentNodeidx, val):
		"""Find the node idx with tne requested val if exists."""
		currentNode = self.tree[currentNodeidx]
		if currentNode['val'] == val:
			currentidx = currentNodeidx
		elif val <= currentNode['val']:
			leftChild = currentNode['L']
			if leftChild == None:
				raise ValueError('Value not found in the tree.')
			else:
				currentidx = self._findNode(leftChild, val)
		elif val > currentNode['val']:
			rightChild = currentNode['R']
			if rightChild == None:
				raise ValueError('Value not found in the tree.')
			else:
				currentidx = self._findNode(rightChild, val)
		return currentidx

	def findMin(self, rootidx):
		"""Wrapper for down, find the minimum node in the subtree with rootidx."""
		minNodeidx = self._downleft(rootidx)
		return minNodeidx

	def _downleft(self, currentNodeidx):
		"""Propagate down to the left tree."""
		currentNode = self.tree[currentNodeidx]
		leftChild = currentNode['L']
		if leftChild == None:
			minNodeidx = currentNodeidx
		else:
			nextNodeidx = leftChild
			minNodeidx = self._downleft(nextNodeidx)
		return minNodeidx

	def findMax(self, rootidx):
		"""Wrapper for up, find the maximum node in the subtree with rootidx."""
		maxNodeidex = self._downright(rootidx)
		return maxNodeidex

	def _downright(self, currentNodeidx):
		"""Propagate down to the right tree."""
		currentNode = self.tree[currentNodeidx]
		rightChild = currentNode['R']
		if rightChild == None:
			maxNodeidx = currentNodeidx
		else:
			nextNodeidx = rightChild
			maxNodeidx = self._downright(nextNodeidx)
		return maxNodeidx

	def findNextLarger(self, val):
		"""Wrapper for nextLarger to get the index of val"""
		curridx = self.find(val)
		largeridx = self._nextLarger(curridx)
		return largeridx

	def _nextLarger(self, currentNodeidx):
		"""Find the next larger element if it exists."""
		currentNode = self.tree[currentNodeidx]
		rightChild = currentNode['R']
		if rightChild != None:
			largeridx = self.findMin(rightChild)
		else:
			largeridx = currentNode['P']
			while (largeridx != None) and (currentNodeidx == self.tree[largeridx]['R']):
				currentNodeidx = largeridx
				largeridx = self.tree[currentNodeidx]['P']
		if largeridx == None:
			largeridx = 'Already the largest element'
		return largeridx

	def findNextSmaller(self, val):
		"""Wrapper for next smaller element if it exists."""
		currentidx = self.find(val)
		smalleridx = self._nextSmaller(currentidx)
		return smalleridx

	def _nextSmaller(self, currentNodeidx):
		"""Find the next smaller element if it exists."""
		currentNode = self.tree[currentNodeidx]
		leftChild = currentNode['L']
		if leftChild != None:
			smalleridx = self.findMax(leftChild)
		else:
			smalleridx = currentNode['P']
			while (smalleridx != None) and (currentNodeidx == self.tree[smalleridx]['L']):
				currentNodeidx = smalleridx
				smalleridx = self.tree[currentNodeidx]['P']
		if smalleridx == None:
			smalleridx = 'Already the smallest element'
		return smalleridx

	def delet(self, val):
		"""Wrapper for deletNode."""
		currentidx = self.find(val)
		self._deletNode(currentidx)

	def _deletNode(self, currentNodeidx):
		# Node is a leaf
		currentNode = self.tree[currentNodeidx]
		if (currentNode['L'] == None) and (currentNode['R'] == None):
			parent = self.tree[currentNode['P']]
			if parent['L'] == currentNodeidx:
				parent['L'] = None
			else:
				parent['R'] = None
			# Remove currentNode's references
			for key in currentNode:
				currentNode[key] = None
		# Node has 2 children: replace it with the next larger node
		elif (currentNode['L'] != None) and (currentNode['R'] != None):
			successoridx = self._nextLarger(currentNodeidx)
			currentNode['val'] = self.tree[successoridx]['val']
			self._deletNode(successoridx)
		# Node has a single child
		else:
			if currentNode['R'] != None and currentNode['L'] == None:
				childidx = currentNode['R']
				child = self.tree[childidx]
			elif currentNode['L'] != None and currentNode['R'] == None:
				childidx = currentNode['L']
				child = self.tree[childidx]

			child['P'] = currentNode['P']
			parentidx = currentNode['P']
			if parentidx != None:
				parentNode = self.tree[currentNode['P']]
				if parentNode['R'] == currentNodeidx:
					parentNode['R'] = childidx
				else:
					parentNode['L'] = childidx
			else:
				child['P'] = None
			# Remove currentNode's references
			for key in currentNode:
				currentNode[key] = None

	def TreeDepth(self):
		for index in range(len(self.tree)):
			self.tree[index]['D'] = self._nodeDepth(index)

	def updateDepth(self, currentNodeidx):
		newDepth = self._nodeDepth(currentNodeidx)
		self.tree[currentNodeidx]['D'] = newDepth

	def _nodeDepth(self, currentNodeidx):
		"""Compute the node depth for a single node."""
		currentNode = self.tree[currentNodeidx]
		if (currentNode['L'] == None) and (currentNode['R'] == None):
			depth = 0
		else:
			leftChild = currentNode['L']
			rightChild = currentNode['R']
			if (leftChild != None) and (rightChild != None):
				leftDepth = self._nodeDepth(leftChild)
				rightDepth = self._nodeDepth(rightChild)
				depth = max([leftDepth, rightDepth]) + 1
			elif (leftChild == None) and (rightChild != None):
				depth = self._nodeDepth(rightChild) + 1
			else:
				depth = self._nodeDepth(leftChild) + 1
		return depth

	def leftRotate(self, currentNodeidx):
		currentNode = self.tree[currentNodeidx]
		rightChildidx = currentNode['R']
		rightChild = self.tree[rightChildidx]
		rightChild['P'] = currentNode['P']
		if currentNode['P'] != None:
			parent = self.tree[currentNode['P']]
		if parent['L'] == currentNodeidx:
			parent['L'] = rightChildidx
		elif parent['R'] == currentNodeidx:
			parent['R'] = rightChildidx
		currentNode['P'] = rightChildidx
		gLeftChildidx = rightChild['L']
		if gLeftChildidx != None:
			gLeftChild = self.tree[gLeftChildidx]
			gLeftChild['P'] = currentNodeidx
		currentNode['R'] = gLeftChildidx
		rightChild['L'] = currentNodeidx
		self.updateDepth(currentNodeidx)
		self.updateDepth(rightChildidx)

	def rightRotate(self):
		pass

	def balance(self, index):
		pass


# def f(i):
# 	if i ==  0:
# 		x = True
# 	else:
# 		x = f(i-1)
# 	return x

# f(1)

def main():
	bst = BST()
	L1 = [17,5,25,2,11,9,16,7,35,29,38,28,32,8]
	L2 = [17,25,20,35]
	for l in L2:
		bst.insert(l)
	bst.TreeDepth()
	bst.leftRotate(0)
	print(bst.tree)

if __name__ == '__main__':
	main()
