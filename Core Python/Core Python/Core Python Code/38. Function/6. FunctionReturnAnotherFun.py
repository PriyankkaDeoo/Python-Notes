#Function Return another Function
# Example 1
def disp():
	def show():
		return "Show Function"
	print("Disp Function")
	return show

r_sh = disp()
print(r_sh())

# Example 2
def disp(sh):
	print("Disp Function")
	return sh 

def show():
	return "Show Function"

r_sh = disp(show)
print(r_sh())
