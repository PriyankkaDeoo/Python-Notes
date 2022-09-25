from  threading import current_thread
print(current_thread().getName())
mt = current_thread()
print(mt.daemon)
