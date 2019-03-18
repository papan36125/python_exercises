class Node(object):
	def __init__(self, data):
		self.data = data
		self.next_node = None

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.size = 0

	# O(1) !!!
	def insert_start(self, data):
		self.size +=1
		new_node = Node(data)
		if not self.head:
			self.head = new_node
		else:
			new_node.next_node = self.head
			self.head = new_node

	def remove(self, data):
		if self.head is None:
			return
		self.size -=1
		current_node = self.head
		previous_node = None

		while current_node.data != data:
			previous_node = current_node
			current_node = current_node.next_node
		if previous_node is None:
			self.head = current_node.next_node
		else:
			previous_node.next_node = current_node.next_node

	# O(1)
	def get_size(self):
		return self.size

	# O(1)
	def insert_end(self, data):
		self.size += 1
		new_node = Node(data)
		actual_node = self.head

		while actual_node.next_node is not None:
			actual_node = actual_node.next_node

		actual_node.next_node = new_node

	# O(N)
	def traverse_list(self):
		actual_node = self.head

		while actual_node is not None:
			print('{}'.format(actual_node.data))
			actual_node = actual_node.next_node

linked_list = LinkedList()
linked_list.insert_start(12)
linked_list.insert_start(122)
linked_list.insert_start(3)
linked_list.insert_end(31)

linked_list.traverse_list()
print(linked_list.get_size())

linked_list.remove(3)
linked_list.remove(12)
linked_list.remove(122)
linked_list.remove(31)

linked_list.traverse_list()
print(linked_list.get_size())
