#pop(positon_number) method
a = [10, 20, 30, 10, 90, 'Geekyshows']

print("Before POP:", a)

n = a.pop(2)

print("After POP:", a)

for element in a:
	print(element)
	
print("Removed Element:",n)