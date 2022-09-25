# Getting input from user in 2D Array using while Loop Numpy
from numpy import *
m = int(input("Enter Number of Rows: "))
n = int(input("Enter Number of Columns: "))
a = zeros((m, n), dtype=int)
u = len(a)
i = 0
while(i<u):
	j = 0
	while j < len(a[i]):
		x = int(input("Enter Element: "))
		a[i][j] = x
		j+=1
	i+=1

i = 0
while i < u :
	j = 0
	while j < len(a[i]):
		print('index',i,j,"=",a[i][j])
		j+=1
	i+=1
	
print(type(a))
