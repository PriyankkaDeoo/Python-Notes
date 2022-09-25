from abc import ABC, abstractmethod
class Father(ABC):

	@abstractmethod					
	def disp(self):					# Abstract Method
		pass
		
	def show(self):					# Concrete Method
		print('Concrete Method')
		
#my = Father()						# Not possible to create object of a abstract class

class Child(Father):
	def disp(self):
		print("Defining Abstract Method")
		

c = Child()
c.disp()
c.show()


