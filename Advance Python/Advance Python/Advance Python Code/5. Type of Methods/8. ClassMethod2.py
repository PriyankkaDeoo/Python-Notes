# Class Method w/o Parameter
class Mobile:
	fp = 'Yes'						# Class Variable
	
	@classmethod
	def show_model(cls):			# Class Method
		# Accessing Class Variable
		print("Fingerprint Scaner:", cls.fp)	

realme = Mobile()
Mobile.show_model()					# Calling Class Method