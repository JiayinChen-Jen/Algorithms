from graphviz import Digraph

class BST(object):
	"""A node is defined as a dictionary of
	{'val': val, 'P': index of parent, 'L': index of left child, 'R': index of right child}
	"""
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
		self.TreeDepth()

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

	def printTree(self):
		dot = Digraph(comment='Binary search tree')
		dot.attr(ordering='out')
		for ind in range(len(self.tree)):
			if self.tree[ind]['P'] == None and self.tree[ind]['val'] != None:
				rootidx = ind
		self._print(rootidx, dot)
		# print(dot.source)
		dot.render('bst.gv', view=True)

	def _print(self, currentNodeidx, dot):
		"""generate nodes and edges for graphviz. dot is the graphviz object."""
		currentNode = self.tree[currentNodeidx]
		if currentNode['P'] == None:
			dot.node(str(currentNodeidx), str(currentNode['val']))
		leftChildidx = currentNode['L']
		rightChildidx = currentNode['R']
		if leftChildidx != None:
			leftChild = self.tree[leftChildidx]
			dot.node(str(leftChildidx), str(leftChild['val']))
			dot.edge(str(currentNodeidx), str(leftChildidx))
			self._print(leftChildidx, dot)
		if rightChildidx != None:
			rightChild = self.tree[rightChildidx]
			dot.node(str(rightChildidx), str(rightChild['val']))
			dot.edge(str(currentNodeidx), str(rightChildidx))
			self._print(rightChildidx, dot)


