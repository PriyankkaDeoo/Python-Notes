# Instance Variable
class Mobile:
	def __init__(self):
		self.model = 'RealMe X'			# Instance Variable
	
	def show_model(self):				# Instance Method
		print(self.model)				# Accessing Instance Variable

		
realme = Mobile()
redmi = Mobile()
geek = Mobile()

print("RealMe:", realme.model)
print("Redmi:", redmi.model)
print("Geek:", geek.model)
print()
redmi.model = 'Redmi 7s'			# Modifying Instance Variable
print("RealMe:", realme.model)
print("Redmi:", redmi.model)
print("Geek:", geek.model)
