# Reading Data with r mode
f = open('student.txt', mode='r')
data1 = f.readline()
data2 = f.readline()
print(data1)
print(data2)
f.close()