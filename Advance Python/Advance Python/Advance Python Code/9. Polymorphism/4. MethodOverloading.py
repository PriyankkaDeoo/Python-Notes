# Method Overloading
class Myclass:
	def sum(self, a=None, b=None, c=None):
		if a!=None and b!=None and c!=None:
			s = a + b + c
		elif a!=None and b!=None:
			s = a + b
		else:
			s = 'Provide at least Two Numbers'
		return s
		
obj = Myclass()
print(obj.sum(10, 20, 30))