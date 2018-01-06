"""Single linked list for stack implementation."""
from graphviz import Graph
class Node(object):
	"""single linked node"""
	def __init__(self, key):
		self.key = key
		self.next = None

class singlelinked_stack(object):
	def __init__(self):
		self.sentinel = Node(None)
		self.sentinel.next = self.sentinel

	def stack_empty(self):
		return self.sentinel.next == self.sentinel

	def push(self, key):
		node = Node(key)
		node.next = self.sentinel.next
		self.sentinel.next = node

	def pop(self):
		if self.stack_empty():
			raise ValueError('stack underflow')
		x = self.sentinel.next
		self.sentinel.next = x.next
		return x

	def printStack(self): 
		sl = Graph('singlylinked', node_attr={'shape':'record'})	
		if self.stack_empty():
			pass
		else:
			self._draw(self.sentinel.next, sl)
		sl.render('singlylinked.gv', view=True)

	def _draw(self, node, sl):
		if node!= self.sentinel:
			key = str(node.key)
			sl.node(key)
			nextNode = node.next
			if nextNode != self.sentinel:
				nextKey = str(nextNode.key)
				sl.node(nextKey)
				sl.edge(key, nextKey)
				grandNode = nextNode.next
				self._draw(nextNode, sl)		

def main():
	st = singlelinked_stack()
	L = [1, 6, 7, 2, 3]
	for l in L:
		st.push(l)
	st.pop()
	st.pop()
	st.printStack()

if __name__ == '__main__':
	main()