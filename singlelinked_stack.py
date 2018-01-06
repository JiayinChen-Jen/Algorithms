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
			self._draw(self.sentinel.next, 0, sl)
		sl.render('singlylinked.gv', view=True)

	def _draw(self, node, ind, sl):
		if node != self.sentinel:
			key = str(node.key)
			sl.node(str(ind), key)
			nextNode = node.next
			ind += 1
			if ind == 0:
				self._draw(nextNode, ind, sl)
			else:
				sl.edge(str(ind-1), str(ind))
				self._draw(nextNode, ind, sl)



def main():
	st = singlelinked_stack()
	L = [1, 6, 7, 2, 3, 10, 11, 11, 11, 11]
	for l in L:
		st.push(l)
	# st.pop()
	st.printStack()

if __name__ == '__main__':
	main()