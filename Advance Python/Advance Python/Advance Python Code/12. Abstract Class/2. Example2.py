from abc import ABC, abstractmethod

class DefenceForce (ABC):
	def __init__(self):
		self.id = 101
		
	@abstractmethod
	def area(self):
		pass
	
	def gun(self):
		print("Gun = AK47")
		
class Army(DefenceForce):
	def area(self):
		print("Army Area = Land", self.id)
		
class AirForce(DefenceForce):
	def area(self):
		print("AirForce Area = Sky", self.id)
		
class Navy(DefenceForce):
	def area(self):
		print("Navy Area = Sea", self.id)
		
a = Army()
af = AirForce()
n = Navy()

a.gun()
a.area()
print()
af.gun()
af.area()
print()
n.gun()
n.area()

