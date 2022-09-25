# This Method Overloading Concept is not available in Python
# So it will show error
class Myclass:
	def sum(self, a):
		print("1st Sum Method", a)
		
	def sum(self):
		print("2nd Sum Method")		
		
obj = Myclass()
obj.sum()
obj.sum(10)