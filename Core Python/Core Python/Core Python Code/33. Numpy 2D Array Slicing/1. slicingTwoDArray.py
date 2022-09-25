# Slicing 2D Array
from numpy import *
n = array([[10, 20, 30], 
		   [40, 50, 60], 
		   [70, 80, 90]])
print("Original Array")
print(n)

print("0th Row All Columns")	
# 0th Row All Columns
a = n[0, :]
for i in a:
		print(i)

print("1st Row All Columns")
# 1st Row All Columns
b = n[1, :]
for i in b:
		print(i)

print("2nd Row All Columns")
# 2nd Row All Columns
c = n[2, :]
for i in c:
		print(i)

print("0th Column All Rows")
# 0th Column All Rows
d = n[:, 0]
for i in d:
		print(i)

print("1st Column All Rows")
# 1st Column All Rows
e = n[:, 1]
for i in e:
		print(i)

print("2nd Column All Rows")
# 2nd Column All Rows
f = n[:, 2]
for i in f:
		print(i)


print("Element 10, 0th row 0th column")
g = n[0:1, 0:1]
print(g)

print("Element 90, 2nd row 2nd column")
h = n[2:3, 2:3]
print(h)

print("0th row and 1st row of 1st column and 2nd column")
h = n[0:2, 1:3]
print(h)	