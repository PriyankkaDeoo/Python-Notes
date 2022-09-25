# Modifying 2D Array Element
from numpy import *
a = array([[10, 20, 30, 40], [50, 60, 70, 80]])

a[1][2] = 100

n = len(a)
for i in range(n):
	for j in range(len(a[i])):
		print('index',i,j,"=",a[i][j])
	print()
