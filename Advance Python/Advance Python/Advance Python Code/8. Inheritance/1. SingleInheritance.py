# Single Inheritance
class Father:					# Parent Class
	money = 1000
	
	def show(self):
		print("Parent Class Instance Method")
		
	@classmethod
	def showmoney(cls):
		print("Parent Class Class Method:", cls.money)
		
	@staticmethod
	def stat():
		a = 10
		print("Parent Class Static Method:", a)
		
class Son(Father):				# Child Class
	def disp(self):
		print("Child Class Instance Method")

s = Son()
s.disp()
s.show()
s.showmoney()
s.stat()