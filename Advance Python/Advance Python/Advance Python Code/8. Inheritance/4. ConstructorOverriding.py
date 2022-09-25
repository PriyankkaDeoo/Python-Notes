# Constructor Overriding
class Father:					# Parent Class
	def __init__(self):
		self.money = 1000
		print("Father Class Constructor")
		
	def show(self):
		print("Father Class Instance Method")
		
		
class Son(Father):				# Child Class
	def __init__(self):
		self.money = 5000
		self.car = 'BMW'
		print("Son Class Constructor")
		
	def disp(self):
		print("Son Class Instance Method")

s = Son()
print(s.money)
print(s.car)
s.disp()
s.show()
