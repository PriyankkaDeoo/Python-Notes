# Multiple Inheritance
class Father:
	def __init__(self):
		print("Father Class Constructor")
	def showF(self):
		print("Father Class Method")
		
class Mother:
	def __init__(self):
		print("Mother Class Constructor")
	def showM(self):
		print("Mother Class Method")
		
class Son(Father, Mother):
	def __init__(self):
		super().__init__()					# Calling Parent Class Constructor
		print("Son Class Constructor")
	def showS(self):
		print("Son Class Method")
		
		
s = Son()
s.showF()
s.showM()
s.showS()


