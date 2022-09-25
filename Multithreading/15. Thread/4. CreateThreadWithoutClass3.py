# Importing Thread Class from threading Module
from threading import Thread

def disp(a, b):
	print("Thread Running:", a, b)

for i in range(5):
	# Creating Thread Class Object
	t = Thread(target=disp, args=(10, 20))

	# Starting Thread
	t.start()
