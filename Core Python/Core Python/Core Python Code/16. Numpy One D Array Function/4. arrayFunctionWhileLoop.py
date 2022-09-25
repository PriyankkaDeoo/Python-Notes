# 1D Array using array Function Numpy
from numpy import *
stu_roll = array([101, 102, 103, 104, 105])

n = len(stu_roll)
i = 0
while i < n:
	print('index',i,'=',stu_roll[i])
	i+=1