''' queue 

	quite british indeed
	thomas moll 2015
'''

class Queue(object):

	def __init__(self):
		self.front = None
		self.back = None
		self.size = 0

	def __str__(self):
		# TODO implement this later
		pass

	def __len__(self):
		return self.size

	def enqueue(self, item):

		if self.front is None:
			new_node = QueueNode(item)
			self.front = new_node
			self.back = new_node
		else: 
			new_back = QueueNode(item)
			self.back.next = new_back
			self.back = new_back

		self.size += 1

	def dequeue(self):
		if self.front is None:
			raise ValueError()
		else:
			front_node = self.front
			self.front = self.front.next
			self.size -= 1
			return front_node.data

	def peek(self):
		if self.front is None:
			return None
		return self.front.data

	def clear(self):
		self.size = 0 
		self.front = None
		self.back = None

class QueueNode(object):
	def __init__(self, item):
		self.data = item
		self.next = None