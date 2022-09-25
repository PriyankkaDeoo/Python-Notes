# Constructor Overriding with Parameter
class Father:					# Parent Class
	def __init__(self, m):
		self.money = m
		print("Father Class Constructor")
		
	def show(self):
		print("Father Class Instance Method")
		
		
class Son(Father):				# Child Class
	def __init__(self, r):
		self.money = r
		self.car = 'BMW'
		print("Son Class Constructor")
		
	def disp(self):
		print("Son Class Instance Method")

s = Son(2000)
print(s.money)
print(s.car)
s.disp()
s.show()
