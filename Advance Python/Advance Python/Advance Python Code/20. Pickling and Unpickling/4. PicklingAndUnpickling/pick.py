#pick.py
# Storing Object in the file
import pickle, stu
n = int(input('Enter Number of Students: '))
#f = open('student.dat', mode='wb')
with open('student.dat', mode='wb') as f:
	for i in range(n):
		name = input('Enter Student Name: ')
		roll = int(input('Enter Roll: '))
		address = input('Enter Address: ')
		stu1 = stu.Student(name, roll, address)
		pickle.dump(stu1, f)
		print()
print('Pickling Done!')
