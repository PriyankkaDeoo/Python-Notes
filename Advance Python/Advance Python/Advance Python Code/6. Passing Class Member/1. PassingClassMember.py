# Passing Members of one Class to Another Class
class Student:
	# Constructor
	def __init__(self, n, r):
		self.name = n
		self.roll = r
		
	# Instance Method
	def disp(self):
		print("Student Name:", self.name)
		print("Student Roll:", self.roll)
		
class User:
	# Static Method
	@staticmethod
	def show(s):
		print("User Name:", s.name)
		print("User Roll:", s.roll)
		s.disp()
		
# Creating Object of Student Class
stu = Student('Rahul', 101)

# Calling Static Method of User Class and passing object stu as argument
User.show(stu)
		
		