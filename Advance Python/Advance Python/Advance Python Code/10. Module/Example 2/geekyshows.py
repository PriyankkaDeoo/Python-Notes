# geekyshows.py <--- Main Module

import cal								# Importing Cal Module

print("cal Module's variable:", cal.a)	# Accessing Cal Module's Variable

cal.name()								# Accessing Cal Module's Function

add = cal.add		# Accessing and Assigning Module's Function to Variable
a = add(10, 20)							# Accessing Cal Module's Function
print(a)

b = cal.sub(20, 10)						# Accessing Cal Module's Function
print(b)
