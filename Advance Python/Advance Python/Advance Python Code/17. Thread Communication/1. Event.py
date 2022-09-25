from  threading import Thread, Event
from time import sleep
def light_switch():
	sleep(3)
	e.set()
	print("Green Light ON")
	sleep(5)
	print("Red Light ON")
	e.clear()
	
def traffic():
	e.wait()
	while e.is_set():
		print("You can Go....")
		sleep(.5)
	print("Program Done")
	
e = Event()
t1 = Thread(target=light_switch)
t2 = Thread(target=traffic)
t1.start()
t2.start()