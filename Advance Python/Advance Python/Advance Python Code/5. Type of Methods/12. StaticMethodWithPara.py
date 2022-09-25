# Static Method with Parameter
class Mobile:
	
	@staticmethod
	def show_model(m, p):				# Static Method
		model = m
		price = p
		print("Model:", model, "Price", price)	

realme = Mobile()
Mobile.show_model('RealMe X', 1000)		# Calling Static Method