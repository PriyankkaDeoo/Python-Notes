import pickle
class Student:
	def __init__(self, name, roll, address):
		self.name = name
		self.roll = roll
		self.address = address
		
	def disp(self):
		print(f'Name: {self.name} Roll: {self.roll} Address: {self.address}')
		
with open('student.dat', mode='wb') as f:
	stu1 = Student('Rahul', 101, 'Ranchi')
	pickle.dump(stu1, f)
	print('Pickling Done!')
	
with open('student.dat', mode='rb') as f:
	obj = pickle.load(f)
	print('Unpickling Done!')
	obj.disp()