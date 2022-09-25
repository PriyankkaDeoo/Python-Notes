# Example 1
def decor(fun):
	def inner():
		a = fun()
		add = a + 5
		return add
	return inner
	
def num():
	return 10
	
result_fun = decor(num)
print(result_fun())

# Example 2
def decor(fun):
	def inner():
		a = fun()
		add = a + 5
		return add
	return inner
@decor	
def num():
	return 10
	
#result_fun = decor(num)
#print(result_fun()) instead this directcly call num function
print(num())