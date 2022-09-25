# Instance Method with Parameter
class Mobile:
	def __init__(self):
		self.model = 'RealMe X'				# Instance Variable
	
	def show_model(self, p):				# Instance Method with Parameter
		self.price = p
		# Accessing Instance Variable
		print("Model:", self.model, "Price:", self.price)			

realme = Mobile()
realme.show_model(1000)							# Calling Instance Method