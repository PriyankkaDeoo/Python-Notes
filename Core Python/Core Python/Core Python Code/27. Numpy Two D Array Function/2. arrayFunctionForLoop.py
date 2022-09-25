# Accessing 2D Array using for Loop
from numpy import *
a = array([[10, 20, 30, 40], [50, 60, 70, 80]])

for r in a:
	for c in r:
		print(c)
	print()
