# Static Method w/o Parameter
class Mobile:
	fp = 'Yes'						# Class Variable
	
	@staticmethod
	def show_model():				# Static Method
		# Accessing Class Variable
		print("Fingerprint Scaner:", Mobile.fp)	

realme = Mobile()
Mobile.show_model()					# Calling Static Method