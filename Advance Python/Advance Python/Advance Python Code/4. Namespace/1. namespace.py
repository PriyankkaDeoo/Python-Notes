# Class Variable - NameSpace
class Mobile:
	fp = 'Yes'								# Class Variable
		
	@classmethod							# Class Method
	def is_fp(cls):
		print("Finger Print:", cls.fp)		# Accessing Class Variable

		
realme = Mobile()
redmi = Mobile()
geek = Mobile()

print("Class FP:", Mobile.fp)
print("RealMe:", realme.fp)
print("Redmi:", redmi.fp)
print("Geek:", geek.fp)

print()
Mobile.fp = 'No'				# Modifying Class Variable using Class
print("Class FP:", Mobile.fp)
print("RealMe:", realme.fp)
print("Redmi:", redmi.fp)
print("Geek:", geek.fp)
print()
realme.fp = 'Not Working'		# Modifying Class Variable using object
print("Class FP:", Mobile.fp)
print("RealMe:", realme.fp)
print("Redmi:", redmi.fp)
print("Geek:", geek.fp)
print()



