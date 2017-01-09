class Node:
	def __init__(self):
		self.left = None
		self.right =None
		self.data = None
		self.bfactor = 0
class Tree:

	def __init__(self):
		self.size = 0
		self.prev_node = None
		self.data1 = 0
		self.parent = None
		self.child = None
	def create_parent_node(self,data):
		new_node = Node()
		new_node.data = data
		self.present_node = new_node
		self.prev_node = new_node
		return self

	def create_child_node(self,data):
		new_node = Node()
		new_node.data = data
		return new_node

	def height_node(self,node):
		if node is not None:
			return 1 + max(self.height_node(node.left),self.height_node(node.right))
		else:
			return 0
	def has_child_node(self,node):
		if node.left or node.right:
			return True
		


	def update_balance_factor(self,data):
		print ("****************************************")
		node = self.prev_node
		key = data
		while (self.has_child_node(node)):
			node.bfactor = (self.height_node(node.left)-self.height_node(node.right))
			print node.bfactor
			if node.data > key:
				node = node.left # add data condition to iterate node
			else:
				node = node.right
		return self		
	
	
	def get_node_left(self,node):
		self.node = node
		if self.node == None:
			return self
		else:			
			self.prev_node = self.node.left
			return self.prev_node
	

	def get_node_right(self,node):
		self.node = node
		if self.node == None:
			return self			
		else:			
			self.prev_node= self.node.right
			return self.prev_node



	def add_node_left(self,prev_node,node):
		self.sum = 0
		self.prev_node = prev_node		
		self.new_node = node
		self.prev_node.left = self.new_node
		self.prev_node = self.present_node
		self.update_balance_factor(node.data)	
		return self
		


	def add_node_right(self,prev_node,node):
		self.sum = 0
		self.prev_node = prev_node		
		self.new_node =node
		self.prev_node.right = self.new_node
		self.prev_node = self.present_node
		self.update_balance_factor(node.data)
		return self	
			
	def insert_node_right(self,node):
		self.prev_node.right = self.new_node
		self.prev_node = self.present_node
		return self

	def insert_node_left(self,node):
		self.prev_node.right = self.new_node
		self.prev_node = self.present_node
		return self
		
	#def delete_node_find(self):


	def preorder_traversal(self,node):
		if node is not None:
			print str(node.bfactor) + str('') + str(node.data)
			self.preorder_traversal(node.left)
			self.preorder_traversal(node.right)
			



	def postorder_traversal(self,node):
		self.node = node
		if node is not None:
			self.postorder_traversal(node.left)
			self.postorder_traversal(node.right)
			print node.data
			

	def preorder(self):
		print(self.present_node.data)
		if self.present_node.left:
			self.present_node.left.preorder()
		if self.present_node.right:
			self.present_node.right.preorder()


	def inorder_traversal(self,node):
		if node is not None:
			self.inorder_traversal(node.left)
			print node.data	
			self.inorder_traversal(node.right)

		


	def level_traversal(self):
	
		self.levels = 0
		self.present_node = None
		self.prev_node = None
		self.first_node = None
		

	def binary_search_tree(self,node,data,counter):		
		data1 = data
		self.counter = counter
		if counter == 0:
			self.create_parent_node(data)
		else:
			print("into the loop with values")

			while (node):
				print node.data
				print node.left
				print node.right
				if (node.data > data1 and node.left == None ):
					a = self.create_child_node(data1)
					self.add_node_left(node,a).tweak_tree(data1)
					break
				elif (node.data < data1 and node.right == None):
					b = self.create_child_node(data1)
					self.add_node_right(node,b).tweak_tree(data1)
					break
				elif(node.data > data1 and node.left != None):
					node = self.get_node_left(node)
					print node.data
				elif (node.data < data1 and node.right != None):
					node = self.get_node_right(node)
					print node.data
				else:
					print("there is error")
					break
		return self
		

	def tweak_tree(self,data1):
			node = self.prev_node
			self.parent = node
			while (node):
				print ("into tweaking")
				if (node.bfactor  == 2 and node.left.bfactor == 1):
						print("into LL")
						self.LL_rotation(node,data1)
						break
				elif (node.bfactor == -2 and node.right.bfactor == -1):
						self.RR_rotation(node,data1)
						break
				elif (node.bfactor == 2 and node.left.bfactor == -1):
						self.LR_rotaion(node,node.left)
				elif (node.bfactor == -2 and node.left.bfactor == 1):
						self.RL_rotation(node,node.right)
				elif (node.data > data1):
						self.parent = node
						node = node.left
				elif (node.data < data1):
						self.parent = node
						node = node.right
				else:
					break
			return self
			

	def LL_rotation(self,node,data1):
			parent_node = self.parent
			if node == self.present_node :
				self.present_node = node.left
				print ("rotated successfully")
			parent = node.left
			if parent.right == None:
				node.left.right = node
				parent_node.left = node.left
				node.left = None
				child = parent.right
			else:
				parent_node.left = node.left.right
				parent.right = parent_node
				child = parent.right
			parent_node.bfactor = (self.height_node(parent_node.left)-self.height_node(parent_node.right))
			parent.bfactor = (self.height_node(parent.left)-self.height_node(parent.right))
			child.bfactor = (self.height_node(child.left)-self.height_node(child.right))
			self.prev_node = self.present_node
			return self

	def RR_rotation(self,node,data1):
			self.parent = node
			self.child = node.right
			if node == self.present_node :
				self.present_node = node.right
				print ("rotated successfully")
			node.right.left = node
			node.right = None
			parent = self.present_node
			child = self.present_node.left
			parent.bfactor = (self.height_node(parent.left)-self.height_node(parent.right))
			child.bfactor = (self.height_node(child.left)-self.height_node(child.right))
			self.prev_node = self.present_node
			return self


	def main(self):
		a = [23,12,13,14,15,1]
		btree =  Tree()
		for i in xrange(len(a)):
			btree.binary_search_tree(btree.prev_node,a[i],i)
			print i
			
		
		

