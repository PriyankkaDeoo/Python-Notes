from numpy import *

a = array([10, 20, 30, 40, 50])
b = a.view()
a[1] = 80
b[1] = 300
print(a)
print(b)
print("a", id(a))
print("b", id(b))
