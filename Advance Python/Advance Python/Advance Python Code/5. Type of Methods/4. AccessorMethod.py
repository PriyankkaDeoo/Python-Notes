# Instance Method - Accessor Method / Getter Method
class Mobile:
	def __init__(self):
		self.model = 'RealMe X'				# Instance Variable
	
	def get_model(self):					# Accessor Method				
		return self.model			

realme = Mobile()
m = realme.get_model()						# Calling Accessor Method
print(m)