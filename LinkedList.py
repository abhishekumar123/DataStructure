class Node:
	def __init__(self):
		self.head = None
		self.tail = None

class LinkedList:
	def __init__(self):
		self.curr_node = None
		self.first_node = None
		self.prev_node = None
		self.size = 0

	def create_node(self,data):
		new_node = Node()
		new_node.head = data
		new_node.tail = self.curr_node
		self.curr_node = new_node
		self.prev_node = new_node
		self.first_node = new_node
		self.size +=1

	def add_node_beginning(self,data):
		new_node = Node()
		new_node.head = data
		new_node.tail = self.curr_node

	def add_node_end(self,data,node):
		new_node = Node()
		new_node.head =data
		new_node.tail = None
		node.tail = new_node
		self.prev_node = new_node
		self.size +=1


	def print_list(self,node):
		self.curr_node = node
		while self.curr_node:
			print(self.curr_node.head)
			self.curr_node = self.curr_node.tail

	def get_size(self):
		print(self.size)

	def print_list_end(self):


	def find_n_delete(self,data):

