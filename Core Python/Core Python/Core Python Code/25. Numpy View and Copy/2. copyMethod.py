from numpy import *

a = array([10, 20, 30, 40, 50])
b = copy(a)
a[1] = 80
b[2] = 300
print(a)
print(b)
print("a", id(a))
print("b", id(b))
