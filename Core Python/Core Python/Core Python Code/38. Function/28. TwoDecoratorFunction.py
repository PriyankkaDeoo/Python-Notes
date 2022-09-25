# Two Decorator Function to same function 
# Example 1
def decor(fun):
	def inner():
		a = fun()
		add = a + 5
		return add
	return inner

def decor1(fun):
	def inner():
		b = fun()
		multi = b * 5
		return multi
	return inner
	
def num():
	return 10
	
result_fun = decor(decor1(num))
print(result_fun())

# Example 2
def decor(fun):
	def inner():
		a = fun()
		add = a + 5
		return add
	return inner

def decor1(fun):
	def inner():
		b = fun()
		multi = b * 5
		return multi
	return inner
@decor
@decor1	
def num():
	return 10
	
# result_fun = decor(decor1(num))
# print(result_fun()) instead of this directly call num function
print(num())
