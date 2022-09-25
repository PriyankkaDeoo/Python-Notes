# Nested List - for loop
a = [[10, 20, 30],[40, 50, 60]]
	 
# without index
for r in a:
	for c in r:
		print(c)
	print()

# With Index
n = len(a)
for i in range(n):
	for j in range(len(a[i])):
		print(i, j, a[i][j])
	print ()


