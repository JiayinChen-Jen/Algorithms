from graphviz import Digraph
import numpy
import numpy.random as rand

from binaryTree import BST

class RBT(BST):
	"""Red black tree. """
	def __init__(self):
		super(RBT, self).__init__()

	def createNode(self, val):
		self.tree.append({'val': val, 'P': None ,'L': None, 'R': None, 'C': None})

	def RB_insert(self, val):
		self.insert(val)
		self.tree[-1]['C'] = 'red'
		self.insertFix(len(self.tree)-1)

	def insertFix(self, currentNodeidx):
		"""Fix color when inserting into a RBT."""
		currentNode = self.tree[currentNodeidx]
		parentidx = currentNode['P']
		while (parentidx != None and self.tree[parentidx]['C'] == 'red'):
			parent = self.tree[parentidx]
			grandParentidx = parent['P']
			grandParent = self.tree[grandParentidx]
			if parentidx == grandParent['L']:
				# y is uncle of current node
				yidx = grandParent['R']
				if yidx == None:
					uncleColor = 'black'
				else:
					y = self.tree[yidx]
					uncleColor = y['C']
				if uncleColor == 'red':
					parent['C'] = 'black'
					y['C'] = 'black'
					grandParent['C'] = 'red'
					currentNodeidx = grandParentidx
				elif currentNodeidx == parent['R']:
					currentNodeidx = parentidx
					self.leftRotate(currentNodeidx)
					currentNode = self.tree[currentNodeidx]
					parent = self.tree[currentNode['P']]
					grandParentidx = parent['P']
					grandParent = self.tree[grandParentidx]
					parent['C'] = 'black'
					grandParent['C'] = 'red'
					self.rightRotate(grandParentidx)
				elif currentNodeidx == parent['L']:
					grandParent['C'] = 'red'
					parent['C'] = 'black'
					self.rightRotate(grandParentidx)
					parentidx = currentNode['P']					
			elif parentidx == grandParent['R']:
				yidx = grandParent['L']
				if yidx == None:
					uncleColor = 'black'
				else:
					y = self.tree[yidx]
					uncleColor = y['C']
				if uncleColor == 'red':
					parent['C'] = 'black'
					y['C'] = 'black'
					grandParent['C'] = 'red'
					currentNodeidx = grandParentidx
				elif currentNodeidx == parent['L']:
					currentNodeidx = parentidx
					self.rightRotate(currentNodeidx)
					currentNode = self.tree[currentNodeidx]
					parent = self.tree[currentNode['P']]
					parent['C'] = 'black'
					grandParentidx = parent['P']
					grandParent = self.tree[grandParentidx]
					grandParent['C'] = 'red'
					self.leftRotate(grandParentidx)
				elif currentNodeidx == parent['R']:
					grandParent['C'] = 'red'
					parent['C'] = 'black'
					self.leftRotate(grandParentidx)
					parentidx = currentNode['P']		
								
			currentNode = self.tree[currentNodeidx]
			parentidx = currentNode['P']
		for ind in range(len(self.tree)):
			if self.tree[ind]['val'] != None and self.tree[ind]['P'] == None:
				self.tree[ind]['C'] = 'black'


	def printTree(self):
		"""Add in colors."""
		dot = Digraph(comment='Binary search tree')
		dot.attr(ordering='out')
		for ind in range(len(self.tree)):
			if self.tree[ind]['P'] == None and self.tree[ind]['val'] != None:
				rootidx = ind
		self._print(rootidx, dot)
		dot.render('bst.gv', view=True)

	def _print(self, currentNodeidx, dot):
		currentNode = self.tree[currentNodeidx]
		dot.node_attr.update(shape='circle')
		if currentNode['P'] == None:
			if currentNode['C'] == 'red':
				dot.attr('node', fillcolor='plum1', style='filled')
			else:
				dot.attr('node', fillcolor='black', style='filled', fontcolor='white')
			dot.node(str(currentNodeidx), str(currentNode['val']))
		leftChildidx = currentNode['L']
		rightChildidx = currentNode['R']
		if leftChildidx != None:
			leftChild = self.tree[leftChildidx]
			if leftChild['C'] == 'red':
				dot.attr('node', fillcolor='plum1', style='filled')
			else:
				dot.attr('node', fillcolor='black', style='filled', fontcolor='white')
			dot.node(str(leftChildidx), str(leftChild['val']))
			dot.edge(str(currentNodeidx), str(leftChildidx))
			self._print(leftChildidx, dot)
		if rightChildidx != None:
			rightChild = self.tree[rightChildidx]
			if rightChild['C'] == 'red':
				dot.attr('node', fillcolor='plum1', style='filled')
			else:
				dot.attr('node', fillcolor='black', style='filled', fontcolor='white')
			dot.node(str(rightChildidx), str(rightChild['val']))
			dot.edge(str(currentNodeidx), str(rightChildidx))
			self._print(rightChildidx, dot)

def main():
	rbt = RBT()
	L1 = [11, 2, 1, 7, 14, 5, 4, 8, 15]
	L2 = [38, 13, 51, 10, 12, 40, 84, 25]
	L3 = rand.randint(30, size=20).tolist()
	for l in L2:
		rbt.RB_insert(l)
	print(rbt.tree)
	rbt.printTree()

if __name__ == '__main__':
	main()

