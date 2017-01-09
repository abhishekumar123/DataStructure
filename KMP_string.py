class Kmp:
	def __init__(self):
		self.p_func = []

	def get_prefix(self,inp_str):
		self.prefix_set = []
		for i in xrange(len(inp_str)-1):
			st = ''
			for j in xrange(i+1):
				st = str(st) + str(inp_str[j])
			
			self.prefix_set.append(st)

	
	def get_suffix(self,inp_str):
		self.suffix_set = []
		for i in range(1,len(inp_str)):
			st = ''
			for j in range(i,len(inp_str)):
				st = str(st) + str(inp_str[j])
			self.suffix_set.append(st)

	def get_p_func(self,inp_str):
		for i in  xrange(len(inp_str)):
			st =''
			for j in xrange(i+1):
				st = str(st) + str(inp_str[j])
			self.get_prefix(st)
			self.get_suffix(st)
			self.a = list(set(self.prefix_set) & set(self.suffix_set))
			if len(self.a) == 0:
				self.p_func.append(0)

			else:	
				self.p = max(self.a,key =len)
				self.p_func.append( len(self.p))



	def compare_pattern(self,inp_str,pattern):
		self.get_p_func(inp_str)
		i = 0 
		self.j = [] 
		t = 0
		while (i < len(inp_str)):
			if (inp_str[i] == pattern[t]):
				self.j.append(i)
				t += 1
				i += 1
			else:
				self.j = []
				t = 0
				if(self.p_func[i] == 0):
					i = i+1
				else:
					i = i+ self.p_func[i]


			
