a = [10, 50, 60, 80, 90, 5, 45, 65]

# Without Lambda
def high_marks(n):
	if n >= 60:
		return True

result = list(filter(high_marks,a))
print(result)
print(type(result))

print()

# With Lambda
result = list(filter(lambda n : (n>=60),a))
print(result)
print(type(result))




