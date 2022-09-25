# Constructor
class Mobile:
	# Constructor
	def __init__(self, m, v=80):
		self.model = m
		self.volumn = v
		
	def show_model(self, p):
		price = p				# Local Varaible
		print("Model:", self.model, "and Price:", price)
		print("Volumn:", self.volumn)

# Passing Argument to Constructor
realme = Mobile('Realme X')

# Accessing Method from outside Class
realme.show_model(1000)
