from time import time, ctime, localtime
epoch = time()
print()

print("epoch seconds:", epoch)
print()

et = ctime(epoch)
print("Epoch Date and Time:", et)
print()

ct = ctime()
print("Current Date and Time:", ctime())
print()

stobj = localtime()
print("struct_time Object:", stobj)
print()

print("Year:", stobj.tm_year)
print("Month:", stobj.tm_mon)
print("Date:", stobj.tm_mday)
print("Hour:", stobj.tm_hour)
print("Minute:", stobj.tm_min)
print("Second:", stobj.tm_sec)
print()
print(stobj.tm_mday, end="/")
print(stobj.tm_mon, end="/")
print(stobj.tm_year)
print(stobj.tm_hour, end=":")
print(stobj.tm_min, end=":")
print(stobj.tm_sec)
print()