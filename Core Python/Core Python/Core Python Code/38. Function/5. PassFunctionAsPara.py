#Pass a Function as Parameter
# Example 1
def disp(sh):
	print(type(sh))
	print("Disp Function" + sh())
	
def show():
	return " Show Function"

disp(show)

# Example 2 with return
def disp(sh):
	return "Disp Function" + sh()
	
def show():
	return " Show Function"

result = disp(show)
print(result)
