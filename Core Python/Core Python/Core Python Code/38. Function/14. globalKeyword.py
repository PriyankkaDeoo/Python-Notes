# Global Keyword
#Example 1
a = 50
def show():
	a = 10
	print("A:",a)		# It will show local variable value
show()
print("A:",a)			# It will show global variable value

#Example 2
a = 50
def show():
	global a			
	print("A:",a)
	a = 20				# Modifiying Global Variable value
	print("A:",a)
show()
print("A:",a)			# It will show modified global variable value
