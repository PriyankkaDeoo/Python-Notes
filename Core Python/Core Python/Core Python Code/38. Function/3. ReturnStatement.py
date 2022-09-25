# Return Statement Single Value
#Defining a Function
def add():
	x = 10
	y = 20
	c = x + y
	return c
	
#Calling a Function
sum = add()
print(sum)

#Defining a Function
def add():
	x = 10
	y = 20
	return x + y
	
#Calling a Function
sum = add()
print(sum)

#Defining a Function with Parameter
def add(y):
	x = 10
	return (x + y)
	
#Calling a Function with Argument
sum = add(20)
print(sum)

# Return Statement Multiple Values
#Defining a Function
def add(y):
	x = 10
	c = x + y
	d = y - x
	return c, d, 50
	
#Calling a Function
sum, sub, a = add(20)
print(sum)
print(sub)
print(a)
	

