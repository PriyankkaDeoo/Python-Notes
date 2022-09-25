# Tuple of Lists
a = ([10, 20], [30,40])

print("Original Tuple A:", a)
print(id(a))
print()

# Modifying List
a[0][0] = 80
print("After Modification:",a)
print(id(a))

# Accessing Tuple of Lists using for loop
n = len(a)
for i in range(n):
	for j in range(len(a[i])):
		print(i, j, a[i][j])
	print ()