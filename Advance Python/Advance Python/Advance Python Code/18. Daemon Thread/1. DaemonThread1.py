from  threading import Thread
def disp():
	print('Daemon Thread')
	
t1 = Thread(target=disp)
print('Before:', t1.isDaemon())	
t1.setDaemon(True)
print('After:', t1.isDaemon())
t1.start()