# Getting Input from user in 1D Array using While Loop Numpy
from numpy import *
n = int(input("Enter Number of Elements: "))
a = zeros(n, dtype=int)
u = len(a)
i = 0
j = 0
while(i<u):
	x = int(input("Enter Element: "))
	a[i] = x
	i+=1
	
while(j<(len(a))):
	print(a[j])
	j+=1

print(type(a))