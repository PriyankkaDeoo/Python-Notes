# Function Decorator
# Example 1
def decor(fun):
	def inner():
		print("Inner Function: Before enhancing Function")
		fun()
		print("Inner Function: After enhancing Function")
	return inner
	
def num():
	print("We will use this function")
	print("and will enhance this in decorator")
	
result_fun = decor(num)
result_fun()

# Example 2
def decor(fun):
	def inner():
		print("Inner Function: Before enhancing Function")
		fun()
		print("Inner Function: After enhancing Function")
	return inner
@decor	
def num():
	print("We will use this function")
	print("and will enhance this in decorator")
	
#result_fun = decor(num)
#result_fun() instead this directcly call num function
num()


