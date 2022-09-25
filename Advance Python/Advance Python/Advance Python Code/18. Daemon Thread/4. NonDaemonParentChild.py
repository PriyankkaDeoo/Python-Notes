from threading import Thread, current_thread
def disp():
	print('Disp Function')

mt = current_thread()	
print(mt.getName())
print(mt.isDaemon())
t1 = Thread(target=disp)	# Child of Main Thread becoz created by Main Thread
print(t1.isDaemon())
t1.start()
