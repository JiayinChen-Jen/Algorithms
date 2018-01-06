"""doubly linked list with sentinel"""
from graphviz import Graph
class Node(object):
	def __init__(self, key):
		self.key = key
		self.next = None
		self.prev = None


class doublylinked_list(object):
	def __init__(self):
		self.sentinel = Node(None)
		self.sentinel.next = self.sentinel
		self.sentinel.prev = self.sentinel

	def isEmpyty(self):
		return self.sentinel.next == self.sentinel

	def add(self, key):
		node = Node(key)
		node.next = self.sentinel.next 
		self.sentinel.next.prev = node
		self.sentinel.next = node
		node.prev = self.sentinel

	def search(self, key):
		if self.isEmpyty():
			raise ValueError('linked list is empty')
		node = self.sentinel.next
		while node != self.sentinel and node.key != key:
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
		elif self.sentinel.next == self.sentinel:
			dl.node(str(self.sentinel.key), shape='circular')
		else:
			self._draw(self.sentinel.next, dl)
		dl.render('doublylinked.gv', view=True)

	def _draw(self, node, dl):
		if node!= self.sentinel:
			key = str(node.key)
			dl.node(key)
			nextNode = node.next
			if node.prev != self.sentinel:
				prevKey = str(node.prev.key)
				dl.edge(prevKey, key)
			if nextNode != self.sentinel:
				nextKey = str(nextNode.key)
				dl.node(nextKey)
				dl.edge(key, nextKey)
				grandNode = nextNode.next
				self._draw(grandNode, dl)

def main():
	dl = doublylinked_list()
	L = [1, 2, 3, 5, 6, 7, 10, 0]
	for l in L:
		dl.add(l)
	dl.delet(5)
	dl.delet(6)
	dl.printLinked()

if __name__ == '__main__':
	main()

