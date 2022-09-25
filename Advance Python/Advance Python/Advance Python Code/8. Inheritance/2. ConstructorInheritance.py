# Constructor in Inheritance
class Father:					# Parent Class
	def __init__(self):
		self.money = 1000
		print("Father Class Constructor")
		
	def show(self):
		print("Father Class Instance Method")
		
		
class Son(Father):				# Child Class
	def disp(self):
		print("Son Class Instance Method", self.money)

s = Son()
s.disp()
print("Father Instance Variable:", s.money)
s.show()
