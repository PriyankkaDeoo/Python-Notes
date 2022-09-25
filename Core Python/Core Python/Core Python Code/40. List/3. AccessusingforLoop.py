# Accessing List using for loop
a = [10, 20, -50, 21.3, 'Geekyshows']

#without index
print("Accessing List using for Loop without index")
for element in a:
	print(element)
	
print()

#With Index
print("Accessing List using for Loop with index")
n = len(a)
for i in range(n):
	print(i, "=", a[i])