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
	stu2 = Student('Sonam', 102, 'Dhanbad')
	pickle.dump(stu1, f)
	pickle.dump(stu2, f)
	print('Pickling Done!')
	
with open('student.dat', mode='rb') as f:
	obj1 = pickle.load(f)
	obj2 = pickle.load(f)
	print('Unpickling Done!')
	obj1.disp()
	obj2.disp()
