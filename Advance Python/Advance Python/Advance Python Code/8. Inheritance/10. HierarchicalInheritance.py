# Hierarchical Inheritance
class Father:
	def __init__(self):
		print("Father Class Constructor")
	def showF(self):
		print("Father Class Method")
		
class Son(Father):
	def __init__(self):
		print("Son Class Constructor")
	def showS(self):
		print("Son Class Method")
		
class Daughter(Father):
	def __init__(self):
		print("Daughter Class Constructor")
	def showD(self):
		print("Daughter Class Method")
		
d = Daughter()
d.showF()
d.showD()
s = Son()
s.showF()
s.showS()


