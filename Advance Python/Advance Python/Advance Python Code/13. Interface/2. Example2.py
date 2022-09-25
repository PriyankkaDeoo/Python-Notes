from abc import ABC, abstractmethod

class Father(ABC):
	@abstractmethod
	def disp1(self):
		pass
	@abstractmethod
	def disp2(self):
		pass

class Child(Father):
	def disp1(self):
		print("Child Class")
		print("Disp 1 Abstract Method")
		
class Granchild(Child):
	def disp2(self):
		print("GrandChild Class")
		print("Disp 2 Abstract Method")		
		
gc = Granchild()
gc.disp1()
gc.disp2()
		