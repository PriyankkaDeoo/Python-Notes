# Getting Input from User in 1D Array numpy
from numpy import *
n = int(input("Enter Number of Elements: "))
a = zeros(n, dtype=int)
for i in range(len(a)):
	x = int(input("Enter Element: "))
	a[i] = x
for i in range(len(a)):
	print(a[i])
