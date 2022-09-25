# Importing Thread Class from threading Module
from threading import Thread

def disp():
	pass

# Creating Thread Class Object
t = Thread(target=disp)
print("Default Child Thread Name:",t.getName())
t.setName('Doc Thread')
print("New Child Thread Name:",t.getName())
t.name = 'Flying Thread'
print(t.name)


