# Instance Variable from Outside Class
class Mobile:
	def __init__(self):
		self.model = 'RealMe X'			# Instance Variable
	
	def show_model(self):				# Instance Method
		print(self.model)				# Accessing Instance Variable

		
realme = Mobile()
realme.show_model()
# Accessing Instance Variable from Outside Class
r = realme.model
print("Outside Class:", r)	
