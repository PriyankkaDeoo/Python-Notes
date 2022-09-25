# Creating a thread by creating a child class to Thread class
# Importing Thread Class from threading Module
from threading import Thread

class Mythread(Thread):
	def run(self):
		for i in range(5):
			print("Child Thread")

t = Mythread()
t.start()
t.join()
for i in range(5):
	print("Main Thread")
