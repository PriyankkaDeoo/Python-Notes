# Reading Data with r mode
f = open('student.txt', mode='r')
data = f.readlines()
print(data)
for i in data:
	print(i, end='')
f.close()
