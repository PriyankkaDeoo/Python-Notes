# Class Method with Parameter
class Mobile:
	fp = 'Yes'						# Class Variable
	
	@classmethod
	def show_model(cls, r):			# Class Method
		cls.ram = r
		# Accessing Class Variable
		print("Fingerprint Scaner:", cls.fp, "RAM:", cls.ram)	

realme = Mobile()
Mobile.show_model('4GB')			# Calling Class Method