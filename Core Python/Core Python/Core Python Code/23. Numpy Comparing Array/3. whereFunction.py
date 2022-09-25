from numpy import *
a = array([101, 12, 300, 4, 500])
b = array([100, 20, 30, 400, 50])
result = where(a>b, a, b)
print(result)
