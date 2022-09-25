# Single Tasking using a Thread
from threading import Thread
from time import *
class MyExam:
	def solve_question(self):
		self.task1()
		self.task2()
		self.task3()
		
	def task1(self):
		print("Question 1 Solved")

	def task2(self):
		print("Question 2 Solved")
		
	def task3(self):
		print("Question 3 Solved")

mye = MyExam()
t = Thread(target=mye.solve_question)
t.start()		