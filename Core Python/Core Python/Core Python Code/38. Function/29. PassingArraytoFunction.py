# Passing Array to Function
from array import *
def show(ar):
	print(ar)
	print(type(ar))
	for i in ar:
		print(i)

a = array('i', [101, 102, 103, 104])
show(a)



