# Operator Overloading
class A:
	def __init__(self, x):
		self.x = x
	def __add__(self, other):
		return self.x + other.x
			
class B:
	def __init__(self, x):
		self.x = x
		
a = A(100)
b = B(200)
print(a+b)		#A.__add__(a, b)

#10+20			int.__add__(10, 20)
#'a'+'b'			str.__add__('a', 'b')
#a+b				A.__add__(a, b)

