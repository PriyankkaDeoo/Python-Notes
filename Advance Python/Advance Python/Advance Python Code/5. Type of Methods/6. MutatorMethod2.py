# Instance Method - Mutator Method / Setter Method
class Mobile:
	def set_model(self, m):					# Mutator Method				
		self.model = m			

realme = Mobile()
realme.set_model('RealMe X')	 			# Calling Mutator Method
print(realme.model)