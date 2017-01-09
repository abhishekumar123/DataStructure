class vertex:
	def __init__(self):
		self.vertex = None
		self.connected_to = {}
	def add_neighbour(self,vertex,weight):
		self.connected_to[vertex] = weight
		

class graph:

	def __init__(self):
		self.mapp_dict = {}
		self.arr = []
		self.visited = []
		self.path  = []
		
		
	def create_vertex(self,data):
		new_vertex = vertex()
		new_vertex.vertex = data
		self.mapp_dict[data] = new_vertex
		
		return self
		
		

	def add_connected_vertex(self,key,vertex,weight):
		if key not in self.mapp_dict:
			self.create_vertex(key)
		if vertex not in self.mapp_dict:
			self.create_vertex(vertex)
		self.mapp_dict[key].add_neighbour(vertex,weight)
		self.mapp_dict[vertex].add_neighbour(key,weight)
			

		

	def dfs_traversal(self,vertex):
		self.arr.append(vertex)
		temp = vertex
		while temp:
			for k in self.mapp_dict[temp].connected_to.iterkeys():
				self.arr.append(k)
			self.visited.append(temp)
			self.arr = set(self.arr)-set(self.visited)
			self.arr = list(self.arr)
			try:
				temp = self.arr.pop(-1)
			except Exception:
				print ("traversal done")
				break
	
	
	def bfs_traversal(self,vertex):
		self.arr.append(vertex)
		temp = vertex
		while temp:
			for k in self.mapp_dict[temp].connected_to.iterkeys():
				self.arr.append(k)
			
			try:
				self.visited.append(temp)
				self.arr = (set(self.arr) - set(temp)) 
				self.arr = set(self.arr) - set(self.visited)
				self.arr = list(self.arr)
				temp = self.arr.pop(0)
				
			except Exception:
				print ("traversal done")
				break


			
			
		
			
			
	def add_to_stack(self,data):
		self.visited.append(data)
		
		
		for k in self.mapp_dict[data].connected_to.iterkeys():
			self.arr.append(k)

	def bfs_traversal(self,vertex):

	def topological_traversal(self,vertex):
		






a = graph()

a.add_connected_vertex('a','b',10)

a.add_connected_vertex('b','c',10)

a.add_connected_vertex('b','h',10)

a.add_connected_vertex('c','e',10)

a.add_connected_vertex('c','d',10)

a.add_connected_vertex('e','h',10)

a.add_connected_vertex('e','g',10)
a.add_connected_vertex('e','f',10)

