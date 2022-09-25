# Creating a thread by creating a child class to Thread class
# Importing Thread Class from threading Module
from threading import Thread

class Mythread(Thread):
	def __init__(self):
		Thread.__init__(self)		# Calling Thread Class(Parent) Constructor
		print("Child Thread Constructor")
	def run(self):
		pass

t = Mythread()
t.start()
print("Main Thread")
