"""Elementary data structures"""

class stack(object):
	"""Predefined length n and LIFO policy."""
	def __init__(self, n):
		self.stack = [None for _ in range(n)]
		self.top = -1

	def stack_empty(self):
		if self.top < 0:
			return True
		else:
			return False

	def stack_over(self):
		if self.top > len(self.stack) - 1:
			return True
		else:
			return False

	def push(self, val):
		self.top += 1
		if self.stack_over():
			raise ValueError('stack overflow')
		else:
			self.stack[self.top] = val

	def pop(self):
		if self.stack_empty():
			raise ValueError('stack underflow')
		else:
			x = self.stack[self.top]
			self.stack[self.top] = None
			self.top -= 1
		return x

class doubleStack(object):
	"""Two stacks in an array of length n."""
	def __init__(self, n):
		self.stack = [None for _ in range(n)]
		self.top1 = -1
		self.top2 = len(self.stack)

	def stack_empty(self, name):
		if name == '1':	
			if self.top1 < 0:
				return True
			else:
				return False
		elif name == '2':
			if self.top2 > len(self.stack) - 1:
				return True
			else:
				return False

	def stack_over(self):
		if self.top1 == self.top2:
			return True
		else: 
			return False

	def push(self, val, name):
		if name == '1':
			self.top1 += 1
			if self.stack_over():
				raise ValueError('stack overflow')
			else:
				self.stack[self.top1] = val
		else:
			self.top2 -= 1
			if self.stack_over():
				raise ValueError('stack overflow')
			else:
				self.stack[self.top2] = val

	def pop(self, name):
		if self.stack_empty(name): 
			raise ValueError('stack underflow')
		if name == '1':
			self.stack[self.top1] = None
			self.top1 -= 1
		elif name == '2':
			self.stack[self.top2] = None
			self.top2 += 1


class queue(object):
	"""Predefined length n and FIFO policy."""
	def __init__(self, n):
		self.queue = [None for _ in range(n)]
		self.tail = 0
		self.head = 0

	def queue_empty(self):
		if self.tail == self.head:
			return True
		else: 
			return False

	def queue_over(self):
		if (self.tail+1) % len(self.queue) == self.head:
			return True
		else: 
			return False

	def enqueue(self, val):
		if self.queue_over():
			raise ValueError('queue overflow')
		else:
			self.queue[self.tail] = val
			self.tail = (self.tail + 1) % len(self.queue)

	def dequeue(self):
		if self.queue_empty():
			raise ValueError('queue underflow')
		else:
			x = self.queue[self.head]
			self.queue[self.head] = None
			self.head = (self.head + 1) % len(self.queue)
		return x

class stacks_to_queue(object):
	"""Implement a queue of length n using two stacks.
	st_out stores st_in in reverse order."""
	def __init__(self, n):
		self.st_in = stack(n)
		self.st_out = stack(n)

	def queue_empty(self):
		if self.st_in.top < 0:
			return True
		else:
			return False
	
	def queue_over(self):
		if self.st_in.top > len(self.st_in.stack) - 1:
			return True
		else:
			return False

	def enqueue(self, val):
		"""Efficient enqueue."""
		if self.st_in.stack_over():
			raise ValueError('queue overflow')
		else:
			self.st_in.push(val)

	def dequeue(self):
		"""Inefficient dequeue."""
		if self.st_in.stack_empty():
			raise ValueError('queue underflow')
		else:
			for _ in range(self.st_in.top+1):
				x = self.st_in.pop()
				self.st_out.push(x)
			self.st_out.pop()
			for _ in range(self.st_out.top+1):
				x = self.st_out.pop()
				self.st_in.push(x)

	def print_queue(self):
		print('in stack', self.st_in.stack)
		print('out stack', self.st_out.stack)


class queues_to_stack(object):
	def __init__(self, n):
		self.q1 = queue(n)
		self.q2 = queue(n)

	def stack_empty(self):
		if self.q1.queue_empty():
			return True
		else:
			return False

	def stack_over(self):
		if self.q1.queue_over():
			return True
		else: 
			return False

	def push(self, val):
		"""Efficient push."""
		if self.stack_over():
			raise ValueError('stack overflow')
		else:
			self.q1.enqueue(val)

	def pop(self):
		"""Inefficient pop."""
		print(self.q1.tail)
		if self.stack_empty():
			raise ValueError('stack underflow')
		else:
			if self.q1.tail <= 1:
				x = self.q1.dequeue()
			else:
				for _ in range(self.q1.tail-1):
					y = self.q1.dequeue()
					self.q2.enqueue(y)
				x = self.q1.dequeue()
				self.q1.head = 0
				self.q1.tail = 0				
				for _ in range(self.q2.tail):
					y = self.q2.dequeue()
					self.q1.enqueue(y)
				self.q2.head = 0
				self.q2.tail = 0
		return x

	def print_stack(self):
		print('in queue', self.q1.queue)
		print('out queue', self.q2.queue)

"""doubly linked list."""
class Node(object):
	def __init__(self, key):
		


def main():
	s = queues_to_stack(4)	
	for ind in range(3):
		s.push(ind)
	s.pop()
	s.push(5)
	s.pop()
	s.push(6)
	s.pop()
	s.print_stack()


if __name__ == '__main__':
	main()
