# Importing Thread Class from threading Module
from threading import Thread

def disp():
	pass

# Creating Thread Class Object
t = Thread(target=disp, name='Raj Thread')
print(t.name)


