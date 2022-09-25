# Instance Method - Mutator Method / Setter Method
class Mobile:
	def __init__(self):
		self.model = 'RealMe X'				# Instance Variable
	
	def set_model(self):					# Mutator Method				
		self.model = 'RealMe 2'			

realme = Mobile()
# Before setting
print(realme.model)
# After Setting
realme.set_model()						# Calling Mutator Method
print(realme.model)