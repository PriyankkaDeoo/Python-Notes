#Keyword Variable Length Arguments
#Example 1
def add(**num):
	z = num['a']+num['b']+num['c']
	print("Addition:", z)
	
add(a=5, b=2, c=4)

#Example 2
def add(x, **num):
	z = x+num['a']+num['b']
	print("Addition:", z)
	
add(3, a=5, b=2)
