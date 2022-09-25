# Nested Tuple - for loop
a = (10, 20, 30, (50, 60))
n = len(a)
for i in range(n):
	if type(a[i]) is tuple: 
		if len(a[i])>1:
			m = len(a[i])
			for j in range(m):
				print(i,j, a[i][j])
	else:
		print(i, a[i])
