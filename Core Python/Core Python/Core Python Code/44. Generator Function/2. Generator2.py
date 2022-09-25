def disp(a,b):
	yield a
	yield b
	
result = disp(10, 20)

print(result)
print(type(result))

print(next(result))
print(next(result))


