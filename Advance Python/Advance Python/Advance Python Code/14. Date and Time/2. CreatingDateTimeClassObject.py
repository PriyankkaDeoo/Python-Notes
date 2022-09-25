# Creating Object of datetime Class
from datetime import datetime
dt1 = datetime(year=2019, month=6, day=30)
dt2 = datetime(year=2018, month=5, day=29, hour=15, minute=34)
dt3 = datetime(2017, 4, 28)
dt4 = datetime(2016, 3, 27, 14, 30)
print(dt1)
print(dt2)
print(dt3)
print(dt4)
print(dt1.year)
print(dt2.month)
print(dt3.day)
print(dt4.hour)