# List of Tuples
a = [(10, 20), (30,40)]

print("Original List A:", a)
print(id(a))
print()

# Appending a new Tuple
a.append((50, 60))
print("After Appending a tuple A:",a)
print(id(a))

# Accessing List of Tuple using for loop
n = len(a)
for i in range(n):
	for j in range(len(a[i])):
		print(i, j, a[i][j])
	print ()