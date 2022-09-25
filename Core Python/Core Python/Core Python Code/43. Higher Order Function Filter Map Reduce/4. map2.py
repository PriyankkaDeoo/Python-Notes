a = [10, 20, 30, 40, 50]
b = [1, 2, 3, 4, 5]

# With Lambda
result = list(map(lambda n, m: m+n, a, b))
print(result)
print(type(result))

