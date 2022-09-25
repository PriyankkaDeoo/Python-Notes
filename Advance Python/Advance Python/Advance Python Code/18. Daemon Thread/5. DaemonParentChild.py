from threading import Thread, current_thread

def disp():
	print('Disp Function')
	t2 = Thread(target=show)	# Child of t1 Thread becoz created by t1 Thread
	print('T2:', t2.isDaemon())
	t2.start()

def show():
	print('Show Function')

mt = current_thread()	
print(mt.getName())
print('MT:', mt.isDaemon())
t1 = Thread(target=disp)	# Child of Main Thread becoz created by Main Thread
print('T1 Before:', t1.isDaemon())
t1.setDaemon(True)
print('T1 After:', t1.isDaemon())
t1.start()
t1.join()
