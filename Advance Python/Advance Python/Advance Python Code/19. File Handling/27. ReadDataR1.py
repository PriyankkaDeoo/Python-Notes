# Reading Data with r mode
f = open('student.txt', mode='r')
data = f.read()
print(data)
f.close()
print('Completed!!!!')