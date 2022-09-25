# Creating Object of time Class
from datetime import time
t1 = time(hour=15, minute=34, second=12)
t2 = time(16, 40, 15)
print(t1)
print(t1.hour)
print(t1.minute)
print(t1.second)
print(t1.microsecond)
print()
print(t2)
print(t2.hour)
print(t2.minute)
print(t2.second)