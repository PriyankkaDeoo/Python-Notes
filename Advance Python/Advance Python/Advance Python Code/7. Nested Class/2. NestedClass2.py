# Nested Class
class Army:							# Outer Class
	def __init__(self):
		self.name='Rahul'
		
	def show(self):
		print("Name:", self.name)
		
	class Gun:						# Inner Class
		def __init__ (self):
			self.name = 'AK47'
			self.capacity = '75 Rounds'
			self.length = '34.3 In'
			
		def disp(self):
			print("Gun Name:", self.name)
			print("Capacity:", self.capacity)
			print("Length:", self.length)

a = Army()							# Creating Outer Class Object
print(a.name)
print()
a.show()

print()
g = Army().Gun()					# Creating Inner Class Object
print(g.name)
print(g.capacity)
print(g.length)
print()
g.disp()
	