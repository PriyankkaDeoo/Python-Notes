# Importing Thread Class from threading Module
from threading import Thread

def disp():
	for i in range(5):
		print("Child Thread")

# Creating Thread Class Object
t = Thread(target=disp)

# Starting Thread
t.start()

for i in range(5):
	print("Main Thread")


