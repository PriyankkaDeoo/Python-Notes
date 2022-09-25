# Constructor Parameter with Super Method
class Father:					# Parent Class
	def __init__(self, m):
		self.money = m
		print("Father Class Constructor")
		
	def show(self):
		print("Father Class Instance Method:", self.money)
		
		
class Son(Father):				# Child Class
	def __init__(self, j, m):
		super().__init__(m)		# Calling Parent Class Constructor
		self.job = j
		print("Son Class Constructor")
		
		
	def disp(self):
		print("Son Class Instance Method", self.job)

s = Son('Python', 1000)
s.disp()
s.show()
