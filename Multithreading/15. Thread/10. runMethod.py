# Creating a thread by creating a child class to Thread class
# Importing Thread Class from threading Module
from threading import Thread

class Mythread(Thread):
	def run(self):
		print("Run Method")

t = Mythread()
t.start()