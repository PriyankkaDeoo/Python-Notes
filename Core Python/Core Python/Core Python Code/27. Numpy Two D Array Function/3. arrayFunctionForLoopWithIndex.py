# Accessing 2D Array using for Loop with Index
from numpy import *
a = array([[10, 20, 30, 40], [50, 60, 70, 80]])

n = len(a)
for i in range(n):
	for j in range(len(a[i])):
		print('index',i,j,"=",a[i][j])
	print()
