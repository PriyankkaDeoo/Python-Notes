from numpy import *
a = array([100, 200, 13, 400, 500])
b = array([100, 20, 30, 400, 50])
result1 = a == b
result2 = a < b
result3 = a > b
result4 = a <= b
result5 = a >= b
result6 = a != b
print("a", a)
print("b", b)
print("a==b",result1)
print("a<b",result2)
print("a>b",result3)
print("a<=b",result4)
print("a>=b",result5)
print("a!b",result6)