from array import *
stu_roll = array('i', [101, 102, 103, 104, 105, 106, 107])
print("Original Array")
n = len(stu_roll)
for i in range(n):
	print(i, "=", stu_roll[i])
	
print("From 1st Position to 4th Position")
a = stu_roll[1:5]
for i in a:
	print(i)
	
print("From 0th Position to last Position")
b = stu_roll[0:]
for i in b:
	print(i)
	
print("From 0th Position to 4th Position")
c = stu_roll[:5]
for i in c:
	print(i)

print("Last 4 Elements")
d = stu_roll[-4:]
for i in d:
	print(i)
	
print("From 0th Position to 6th Position stride 2")
e = stu_roll[0:7:2]
for i in e:
	print(i)
	
print("Last 5 Elements with [-5-(-3)]= 2 elements towards right")
f = stu_roll[-5:-3]
for i in f:
	print(i)