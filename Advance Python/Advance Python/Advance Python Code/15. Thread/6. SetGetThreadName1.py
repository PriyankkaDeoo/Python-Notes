# Importing Thread Class from threading Module
from threading import Thread, current_thread

def disp():
	print("Child Thread", current_thread())

	print("Default Child Thread Name:", current_thread().getName())

	current_thread().setName('Doc Thread')
	print("New Child Thread Name:", current_thread().getName())
	
	current_thread().name = 'Flying Thread'
	
	print(current_thread().name)
	

# Creating Thread Class Object
t = Thread(target=disp)

# Starting Thread
t.start()

print("Main Thread", current_thread())

print("Default Main Thread Name:", current_thread().getName())

current_thread().setName('GeekyShows Thread')
print("New Main Thread Name:", current_thread().getName())

current_thread().name = 'Geek Thread'

print(current_thread().name)



