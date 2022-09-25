# 2D Array using ones Function Numpy
from numpy import *
a = ones((3,2), dtype=int)

print("**** Accessing Individual Elements ****")
print(a[0][0])
print(a[0][1])
print(a[1][0])
print(a[1][1])
print(a[2][0])
print(a[2][1])
print()

print("**** Accessing by For Loop ****")
for r in a:
	for c in r:
		print(c)
	print()

print("**** Accessing by For Loop with Index ****")	
n = len(a)
for i in range(n):
	for j in range(len(a[i])):
		print('index',i,j,"=",a[i][j])
	print()

print("**** Accessing by While Loop ****")	
n = len(a)
i = 0
while i < n :
	j = 0
	while j < len(a[i]):
		print('index',i,j,"=",a[i][j])
		j+=1
	i+=1
	print()

