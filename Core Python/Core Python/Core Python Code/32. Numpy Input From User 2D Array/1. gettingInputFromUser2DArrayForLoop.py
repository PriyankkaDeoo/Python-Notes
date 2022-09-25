# Getting input from user in 2D Array using for Loop Numpy
from numpy import *
m = int(input("Enter Number of Rows: "))
n = int(input("Enter Number of Columns: "))
a = zeros((m, n), dtype=int)
u = len(a)

# Input from user
for i in range(u):
	for j in range(len(a[i])):
		x = int(input("Enter Element: "))
		a[i][j] = x

# Accessing 2D Array with index		
for i in range(u):
	for j in range(len(a[i])):
		print('index',i,j,"=",a[i][j])


# Accessing 2D Array without index
for r in a:
	for c in r:
		print(c)
		
print(type(a))
