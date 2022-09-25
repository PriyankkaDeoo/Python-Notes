# writing and then reading It will overwrite existing data
f = open('student.txt', mode='w+')
print(f.tell())
f.write('Youtube')
print(f.tell())
data = f.read()
print(f.tell())
print(data)
