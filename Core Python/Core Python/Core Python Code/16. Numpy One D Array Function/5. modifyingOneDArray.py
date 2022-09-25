# Modifying 1D Array Numpy
from numpy import *
stu_roll = array([101, 102, 103, 104, 105])
stu_roll[1] = 110
n = len(stu_roll)
for i in range(n):
	print('index',i,"=",stu_roll[i])