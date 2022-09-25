# Create Array Example 1
import array
stu_roll = array.array('i', [101, 102, 103, 104, 105])
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

# Create Array Example 2
import array as ar
stu_roll = ar.array('i', [101, 102, 103, 104, 105])
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

# Create Array Example 3
from array import *
stu_roll = array('i', [101, 102, 103, 104, 105])
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

# Create Array Example 4
from array import *
stu_roll = array('f', [10, 20, 10.3, 40, 1.5])
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

# Create Array and iterate using for Loop
from array import *
stu_roll = array('i', [101, 102, 103, 104, 105])
for element in stu_roll:
	print(element)

# Create Array and iterate using for Loop with index
from array import *
stu_roll = array('i', [101, 102, 103, 104, 105])
n = len(stu_roll)
for i in range(n):
	print(i, "=", stu_roll[i])

# Create Array and iterate using while Loop with index
from array import *
stu_roll = array('i', [101, 102, 103, 104, 105])
n = len(stu_roll)
i = 0
while(i<n):
	print(stu_roll[i])
	i+=1


