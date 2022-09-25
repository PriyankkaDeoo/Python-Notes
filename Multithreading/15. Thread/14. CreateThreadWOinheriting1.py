# Creating a thread Without creating a child class to Thread class
# Importing Thread Class from threading Module
from threading import Thread

class Mythread:
	def disp(self, a, b): print(a,b)

myt = Mythread()

t = Thread(target=myt.disp, args=(10, 20))
t.start()

