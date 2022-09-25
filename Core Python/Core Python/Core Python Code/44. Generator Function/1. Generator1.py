# Example 1
def disp(a,b):
	yield a
	yield b
x,y = disp(10, 20)
print(x)
print(y)
print()

# Example 2
def disp(a,b):
	yield a
	yield b
result = disp(10, 20)
print(result)
print(type(result))
# converting to list
lst = list(result)
print(lst)
print(type(lst))


