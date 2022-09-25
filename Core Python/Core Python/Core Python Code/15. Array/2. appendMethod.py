# Append
from array import *
stu_roll = array('i', [101, 102, 103, 104, 105])
n = len(stu_roll)
i = 0
while(i<n):
	print(stu_roll[i])
	i+=1

print("Array After Append")
stu_roll.append(106)
stu_roll.append(107)
n = len(stu_roll)
i = 0
while(i<n):
	print(stu_roll[i])
	i+=1


