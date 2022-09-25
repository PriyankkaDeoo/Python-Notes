# globals ( ) Function 
a = 50
def show():
	a = 10			
	print("Local Variable A:",a)
	x = globals()['a']				
	print("X:",x)
	x = 40
	print("X:",x)
show()
print("Global Variable A:",a)
#print("X:",x)
