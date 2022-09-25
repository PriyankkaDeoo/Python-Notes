# Instance Method w/o Parameter
class Mobile:
	def __init__(self):
		self.model = 'RealMe X'		# Instance Variable
	
	def show_model(self):			# Instance Method
		print("Model:", self.model)	# Accessing Instance Variable

realme = Mobile()
realme.show_model()					# Calling Instance Method