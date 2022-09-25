# DeadLock
from threading import *
l1 = Lock()
l2 = Lock()

def bookticket():
	l1.acquire()
	print('Bookticket Locked on plan')
	print('Bookticket wants to lock Class')
	l2.acquire()
	print('Bookingticket locked seat')
	l2.release()
	l1.release()
	print('Booking ticket done')
	
def cancelticket():
	l2.acquire()
	print('cancelticket Locked on Class')
	print('cancelticket wants to lock Plan')
	l1.acquire()
	print('cancelingticket locked seat')
	l1.release()
	l2.release()
	print('canceling ticket done')	
	
t1 = Thread(target=bookticket)
t2 = Thread(target=cancelticket)
t1.start()
t2.start()
