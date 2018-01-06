"""Single linked list for queue implementation."""
from graphviz import Graph

class Node(object):
	"""single linked node"""
	def __init__(self, key):
		self.key = key
		self.next = None

class singlelinked_queue(object):
	def __init__(self):
		self.sentinel = Node(None)
		# sentinel is the head
		self.sentinel.next = self.sentinel
		self.tail = None

	def stack_empty(self):
		return self.sentinel.next == self.sentinel

	def enqueue(self, key):
		node = Node(key)
		node.next = self.sentinel
		if self.stack_empty():
			self.sentinel.next = node
		else:
			self.tail.next = node
		self.tail = node

	def dequeue(self):
		if self.stack_empty():
			raise ValueError('queue is empty')
		x = self.sentinel.next
		self.sentinel.next = x.next
		return x

	def printQueue(self): 
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
			if ind > 0:
				sl.edge(str(ind-1), str(ind))
			ind += 1
			self._draw(nextNode, ind, sl)



def main():
	st = singlelinked_queue()
	L = [1, 2, 11, 11, 16, 18, 17, 7, 17]
	for l in L:
		st.enqueue(l)
	# print(st.tail.next)
	st.dequeue()
	st.printQueue()

if __name__ == '__main__':
	main()