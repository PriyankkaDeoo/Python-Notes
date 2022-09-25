# Pop(position_number)
from array import *
stu_roll = array('i', [101, 102, 103, 104, 105])
n = len(stu_roll)
i = 0
while(i<n):
	print(stu_roll[i])
	i+=1

print("Array After POP")
r = stu_roll.pop(1)
n = len(stu_roll)
i = 0
while(i<n):
	print(stu_roll[i])
	i+=1
print("Removed Element:", r)