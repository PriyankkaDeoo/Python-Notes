#unpick.py
# Reading Object from the file
import pickle, stu
#f = open('student.dat', mode='rb')
with open('student.dat', mode='rb') as f:
	while True:
		try:
			obj = pickle.load(f)
			obj.disp()
		except EOFError:
			print('Done')
			break
