from binaryTree import BST

class AVL(BST):
	"""Augmented BST with node depth and balancing."""
	def __init__(self):
		super(AVL, self).__init__()

	def createNode(self, val):
		self.tree.append({'val': val, 'P': None ,'L': None, 'R': None, 'D': None})

	def AVL_insert(self, val):
		self.insert(val)
		self.balance(-1)

	def TreeDepth(self):
		"""update the entire tree depth."""
		for index in range(len(self.tree)):
			self.tree[index]['D'] = self._nodeDepth(index)

	def updateDepth(self, currentNodeidx):
		"""update depth of a single node."""
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

	def AVL_leftRotate(self, currentNodeidx):
		currentNode = self.tree[currentNodeidx]
		rightChildidx = currentNode['R']
		parentidx = currentNode['P']
		self.leftRotate(currentNodeidx)
		self.updateDepth(currentNodeidx)
		self.updateDepth(rightChildidx)
		if parentidx != None:
			self.updateDepth(parentidx)

	def AVL_rightRotate(self, currentNodeidx):
		currentNode = self.tree[currentNodeidx]
		leftChildidx = currentNode['L']
		parentidx = currentNode['P']
		self.rightRotate(currentNodeidx)
		self.updateDepth(currentNodeidx)
		self.updateDepth(leftChildidx)
		if parentidx != None:
			self.updateDepth(parentidx)	

	def balance(self, currentNodeidx):
		"""Balance and update tree."""
		while currentNodeidx != None:
			self.TreeDepth()
			currentNode = self.tree[currentNodeidx]
			leftChildidx = currentNode['L']
			rightChildidx = currentNode['R']
			if leftChildidx == None:
				leftHeight = -1
			else:
				leftChild = self.tree[leftChildidx]
				leftHeight = leftChild['D']
			if rightChildidx == None:
				rightHeight = -1
			else:
				rightChild = self.tree[rightChildidx]
				rightHeight = rightChild['D']
			if (leftHeight - rightHeight >= 2):
				gLeftChildidx = leftChild['L']
				gRightChildidx = leftChild['R']
				if gLeftChildidx == None:
					gLeftHeight = -1
				else:
					gLeftChild = self.tree[gLeftChildidx]
					gLeftHeight = gLeftChild['D']
				if gRightChildidx == None:
					gRightHeight = -1
				else:
					gRightChild = self.tree[gRightChildidx]
					gRightHeight = gRightChild['D']
				if (gLeftHeight >= gRightHeight):
					self.rightRotate(currentNodeidx)
				else:
					self.leftRotate(leftChildidx)
					self.rightRotate(currentNodeidx)
			elif (rightHeight - leftHeight >= 2):
				gLeftChildidx = rightChild['L']
				gRightChildidx = rightChild['R']
				if gLeftChildidx == None:
					gLeftHeight = -1
				else:
					gLeftChild = self.tree[gLeftChildidx]
					gLeftHeight = gLeftChild['D']
				if gRightChildidx == None:
					gRightHeight = -1
				else:
					gRightChild = self.tree[gRightChildidx]
					gRightHeight = gRightChild['D']
				if (gRightHeight >= gLeftHeight):
					self.leftRotate(currentNodeidx)
				else:
					self.rightRotate(rightChildidx)
					self.leftRotate(currentNodeidx)
			currentNodeidx = currentNode['P']


def main():
	avl = AVL()
	L1 = [17,5,25,2,11,9,16,7,35,29,38,28,32,8]
	L2 = [17,25,20,35]
	L3 = [41, 20, 65, 11, 29, 50, 26]
	for l in L1:
		avl.AVL_insert(l)
	avl.AVL_insert(23)
	avl.AVL_insert(55)
	avl.printTree()
	# avl.delet(41)
	avl.printTree()
	print(avl.tree)

if __name__ == '__main__':
	main()