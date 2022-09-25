# Local Variable
# Example 1
def show():
	x = 10		# Local Variable
	print(x)	# Accessing Local Variable inside Function
show()
#Accessing Local Variable outside Function
# print(x)		# It will show error

# Example 2
def add(y):
	x = 10		# Local Variable
	print(x)	# Accessing Local Variable inside Function
	print(x+y)	# Accessing Local Variable inside Function

add(20)
#Accessing Local Variable outside Function
# print(x)		# It will show error