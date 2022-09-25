# Global Variable
# Example 1
a = 50
def show():
	x = 10		# Local Variable
	print(x)	# Accessing Local Variable inside Function
	print(a)	# Accessing Global Variable inside Function
show()
# Accessing Global Variable outside Function
print("Global Variable A:",a)	

# Accessing Local Variable outside Function, show error
#print("Global Variable X:",x)

# Example 2 
i = 0
def myfun():
	a = i + 1
	print("My Function", a)
	
myfun()

# Example 3 
i = 0
def myfun():
	# We are trying to increase global variable
	# but remember here i is treated as local variable with same name
	# and as we dont referenced it show it will show error
	i = i + 1
	print("My Function", a)
	
myfun()