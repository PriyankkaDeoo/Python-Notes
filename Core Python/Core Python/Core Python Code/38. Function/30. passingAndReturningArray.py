# Passing and Returning Array
from array import *
def show(ar):
	print("Passed Array ar:",ar)
	print(type(ar))
	for i in ar:
		print(i)
	return ar
print()
a = array('i', [101, 102, 103, 104])
y = show(a)
print("Returning Array Y:",y)
print(type(y))
for i in y:
	print(i)
	


