# Pass/Call by Object Reference 
def val(x):
	x = 15
	print(x, id(x))
	
x = 10
val(x)
print(x, id(x))