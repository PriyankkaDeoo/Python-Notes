# Opening for Writing
f = open('student.txt', mode='w', encoding = 'utf-8')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)
