import os
if os.path.isfile('student.txt'):
	f = open('student.txt')
	print('File Opened')
	f.close()
else:
	print('File Not Found')


