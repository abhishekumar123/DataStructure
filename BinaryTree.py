class Node:
	def __init__(self):
		self.left = None
		self.right =None
		self.data = None

class Tree:

	def __init__(self):
		self.size = 0
	def create_node(self,data):
		new_node = Node()
		new_node.data = data
		self.present_node = new_node
		self.prev_node = new_node
	
	def get_node_left(self,node):
		self.node = node
		if self.node == None:
			return self
		else:			
			self.prev_node = self.node.left
			return self
	

	def get_node_right(self,node):
		self.node = node
		if self.node == None:
			return self			
		else:			
			self.prev_node= self.node.right
			return self



	def add_node_left(self,ref_node,data):
		self.ref_node = ref_node		
		self.new_node =Node()
		self.new_node.data = data
		self.ref_node.left= self.new_node
		self.prev_node = self.present_node	
		return self
		


	def add_node_right(self,ref_node,data):
		self.ref_node = ref_node		
		self.new_node =Node()
		self.new_node.data = data
		self.ref_node.right = self.new_node
		self.prev_node = self.present_node
		return self	
			
		
	#def delete_node_find(self):


	def preorder_traversal(self,node):
		if node is not None:
			print node.data
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
		self.node = node
		if node:
			self.inorder_traversal(self.node.left)
			print self.node.data	
			self.inorder_traversal(self.node.right)

		


	def level_traversal(self,node):
		self.que = []
		self.level_left = 0
		self.level_right = 0
		self.que.append(node)
		while(len(self.que) > 0 ):
			node = self.que.pop(0)
			if(node):
				if(node.left):
					self.que.append(node.left)
					self.level_left += 1
				if(node.right):
					self.que.append(node.right)
					self.level_right +=1

				print node.data
			

	

