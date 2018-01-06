"""doubly linked list."""
from graphviz import Graph
class Node(object):
	def __init__(self, key):
		self.key = key
		self.next = None
		self.prev = None

	def setKey(self, newkey):
		self.key = newkey

	def setNext(self, newnext):
		self.next = newnext

	def setPrevious(self, newprev):
		self.prev = newprev

class doublylinked_list(object):
	def __init__(self):
		self.Lhead = None

	def isEmpyty(self):
		return self.Lhead == None

	def add(self, key):
		node = Node(key)
		node.next = self.Lhead
		if self.Lhead != None:
			self.Lhead.prev = node
		self.Lhead = node
		node.prev = None

	def search(self, key):
		if self.isEmpyty():
			raise ValueError('linked list is empty')
		node = self.Lhead
		while node != None and node.key != key:
			node = node.next
		return node

	def delet(self, key):
		node = self.search(key)
		if node.prev != None:
			node.prev.next = node.next
		else:
			self.Lhead = node.next
		if node.next != None:
			node.next.prev = node.prev

	def printLinked(self):
		dl = Graph('doublylinked', node_attr={'shape':'record'})	
		if self.isEmpyty():
			pass
		elif self.Lhead.next == None:
			dl.node(str(self.Lhead.key))
		else:
			self._draw(self.Lhead, dl)
		dl.render('doublylinked.gv', view=True)

	def _draw(self, node, dl):
		if node!= None:
			key = str(node.key)
			dl.node(key)
			nextNode = node.next
			if node.prev != None:
				prevKey = str(node.prev.key)
				dl.edge(prevKey, key)
			if nextNode != None:
				nextKey = str(nextNode.key)
				dl.node(nextKey)
				dl.edge(key, nextKey)
				grandNode = nextNode.next
				self._draw(grandNode, dl)

def main():
	dl = doublylinked_list()
	L = [1, 2, 3, 5, 6, 7]
	for l in L:
		dl.add(l)
	dl.delet(5)
	dl.delet(6)
	dl.printLinked()

if __name__ == '__main__':
	main()

