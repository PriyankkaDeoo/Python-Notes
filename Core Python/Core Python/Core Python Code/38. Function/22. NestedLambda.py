# Nested Lambda Function
add = lambda x=10 : (lambda y : x + y)
a = add()
print(a)
print(a(20))
