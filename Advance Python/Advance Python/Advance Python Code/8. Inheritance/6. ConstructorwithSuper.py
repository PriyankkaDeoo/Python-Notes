# Constructor with Super Method
class Father:					# Parent Class
	def __init__(self):
		print("Father Class Constructor")
		
	def show(self):
		print("Father Class Instance Method")
		
		
class Son(Father):				# Child Class
	def __init__(self):
		super().__init__()		# Calling Parent Class Constructor
		print("Son Class Constructor")
		
		
	def disp(self):
		print("Son Class Instance Method")

s = Son()
s.disp()
s.show()
