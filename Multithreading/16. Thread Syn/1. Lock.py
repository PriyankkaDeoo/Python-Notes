# Multitasking using Multiple Thread
# Two Threads acting on same method
from threading import *
class Flight:
	def __init__(self, available_seat):
		self.available_seat = available_seat
		self.l = Lock()
		
	def reserve(self, need_seat):
		self.l.acquire(blocking=True)
		print('Available Seats:', self.available_seat)
		if(self.available_seat >= need_seat):
			name = current_thread().name
			print(f'{need_seat} seat is alloted for {name}')
			self.available_seat -= need_seat
		else:
			print('Sorry! All seats has alloted')
		self.l.release()
f = Flight(2)
t1 = Thread(target=f.reserve, args=(1,), name='Rahul')
t2 = Thread(target=f.reserve, args=(1,), name='Sonam')
t3 = Thread(target=f.reserve, args=(1,), name='Raj')
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("Main Thread")
