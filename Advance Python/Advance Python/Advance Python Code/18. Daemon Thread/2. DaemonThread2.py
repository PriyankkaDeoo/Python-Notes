from  threading import Thread
def disp():
	print('Daemon Thread')
	
t1 = Thread(target=disp)
print('Before:', t1.daemon)	
t1.daemon=True
print('After:', t1.daemon)
t1.start()