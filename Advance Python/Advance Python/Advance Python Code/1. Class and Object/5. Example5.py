# Example 5
class Mobile:
	# Constructor
	def __init__(self, m):
		self.model = m
		
	def show_model(self, p):
		price = p				# Local Varaible
		print("Model:", self.model, "and Price:", price)

# Passing Argument to Constructor
realme = Mobile('Realme X')

# Accessing Method from outside Class
realme.show_model(1000)
