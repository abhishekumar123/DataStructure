class Recursion:
	def __init__(self):
		self.fib = []
	def recur(self,data):
		if (data == 0 ):
			return 1
		else:
			self.fib[data -1] =  1 + self.recur(data-1)
			print self.fib[data-1]
			return self.fib[data -1]

			
	def set_list(self,n):
		for i in xrange(n):
			self.fib.append(0)
class Recursive_dp:
	def __init__(self):
		self.fib = []
	def recur_dp(self,n):
		if n == 0:
			 return 1
		elif n == 1:
			 return 1
		if self.fib[n-1] != 0:
			return self.fib[n-1]			
		else:
			self.fib[n-1] = self.recur_dp(n-1) + self.recur_dp(n-2)
			print self.fib[n-1]
			return self.fib[n-1]
		
	def set_list(self,n):
		for i in xrange(n):
			self.fib.append(0)
