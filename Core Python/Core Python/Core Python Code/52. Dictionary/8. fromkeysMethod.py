# Dictionary - fromkeys() Method
key = (101, 102, 103)
value = 'GeekyShows'
d = dict.fromkeys(key, value)
print("New Dict:")
print(d)
print(id(d))
print()

n = dict.fromkeys(key)
print("New Dict:")
print(n)
print(id(n))