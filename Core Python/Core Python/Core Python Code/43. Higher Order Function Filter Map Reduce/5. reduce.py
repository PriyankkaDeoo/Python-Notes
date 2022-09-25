from functools import reduce
a = [10, 20, 30, 40, 50]

result = reduce(lambda n, m: m+n, a)
print(result)
print(type(result))

