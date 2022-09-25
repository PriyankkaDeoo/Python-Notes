# Example 6
class Mobile:
	# Constructor
	def __init__(self, m):
		self.model = m
		
	def show_model(self, p):
		price = p
		print("Model:", self.model, "and Price:", price)

realme = Mobile('RealMe X')
realme.show_model(1000)
print(id(realme))

realme1 = Mobile('RealMe X')
realme1.show_model(1000)
print(id(realme1))

redmi = Mobile('Redmi 7s')
redmi.show_model(2000)
print(id(redmi))

geek = Mobile('Python')
geek.show_model(49)
print(id(geek))
