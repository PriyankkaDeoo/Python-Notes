#Nested Function
# Example 1
def disp():
	def show():
		print("Show Function")
	print("Disp Function")
	show()

disp()

# Example 2 With Return Statement
def disp():
	def show():
		return "Show Function "
	result = show() + "Disp Function"
	return result
print(disp())

# Example 3 With Return Statement and Parameter
def disp(st):
	def show():
		return "Show Function "
	result = show() + st + " Disp Function"
	return result
print(disp("GeekyShows"))