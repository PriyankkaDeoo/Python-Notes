# Example 3
class Mobile:
	def __init__(self):
		self.model = 'RealMe X'
		
	def show_model(self):
		print("Model:", self.model)

# Creating Object of Class
realme = Mobile()

# Accessing Variable from outside class
print(realme.model)

# Assign Variable a new value
realme.model='RealMe Pro2'

print(realme.model)

# Accessing Method from outside class
realme.show_model()


