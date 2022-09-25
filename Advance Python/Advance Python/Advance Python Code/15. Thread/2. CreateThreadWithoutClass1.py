# Importing Thread Class from threading Module
from threading import Thread

def disp():
	print("Thread Running")

# Creating Thread Class Object
t = Thread(target=disp)

# Starting Thread
t.start()
