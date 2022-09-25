a = [10, 20, 30, 40, 50]

# Without Lambda
def inc(n):
	return n+2
	
result = list(map(inc, a))
print(result)
print(type(result))

# With Lambda
result = list(map(lambda n: n+2, a))
print(result)
print(type(result))

