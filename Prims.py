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
	
	def prims (self,vertex,v_stop):
		self.vertice = {}
		self.predecessor = {}
		self.array = {}
		for node in self.visited:
			self.vertice[node] = float(1000.0)
			self.predecessor[node] = None
			self.array[node] = float(1000.0)
		
		self.vertice[vertex] = 0
		self.temp = vertex
		while (self.temp <> v_stop):
			for i in self.mapp_dict[self.temp].connected_to.items():
				if(self.array[i[0]] == 1000):
					self.update_distance(i[0],i[1])
				else:
					self.update_distance(i[0],i[1])
			
		
			self.path.append(self.temp)
			t = priority_queue()
			self.array1 = self.array.copy()	
			self.vertice = self.array.copy()
			
			self.entries_to_remove()
			for vertex,dist in self.array1.iteritems():
				t.insert_heap(dist)
			self.tmp= t.arr.pop(0)
			for vertex,dist in self.array1.iteritems():
				if self.tmp == dist:
					self.temp = vertex

				
				
	
	def entries_to_remove(self):
	    for key in self.path:
		if key in self.array1:
		    del self.array1[key]
	def update_predecessor(self,node):
		self.predecessor[node] = self.temp
			
	def update_distance(self,node,weight):
		if (self.array[node] > self.vertice[self.temp]):
			self.array[node] = self.vertice[self.temp]
			self.update_predecessor(node)	
		
class priority_queue:

	def __init__(self):
		self.arr = [] 

	def insert_heap(self,data):
		self.arr.append(data)
		if (len(self.arr) > 1):
			self.heapify_last()

	def heapify(self):
		for i in xrange(len(self.arr)):
			first_child = 2*i+1
			if(first_child < len(self.arr)):
				if (self.arr[i] > self.arr[first_child]):
					self.swap(i,first_child)

			second_child = 2*i+2
			if(second_child < len(self.arr)):
				if (self.arr[i] > self.arr[second_child]):
					self.swap(i,second_child)
	def heapify_last(self):
		position = len(self.arr)- 1
		while (position > 0):
			
			parent = (position-1)/2
			if (self.arr[parent] > self.arr[position]):
				self.swap(parent,position)
			position = parent
			

	def swap(self,i,j):
		print ("swap")
		self.temp1 = self.arr[i]
		self.arr[i] = self.arr[j]
		self.arr[j] = self.temp1





a = graph()

a.add_connected_vertex('a','b',6)

a.add_connected_vertex('a','c',4)


a.add_connected_vertex('c','b',1)

a.add_connected_vertex('c','d',3)

a.add_connected_vertex('b','d',1)

a.add_connected_vertex('d','e',9)

a.add_connected_vertex('b','e',2)
a.add_connected_vertex('e','f',9)

