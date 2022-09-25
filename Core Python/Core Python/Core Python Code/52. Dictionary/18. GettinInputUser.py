# Getting input from user

# Creating Empty Dict
a = {}

n = int(input("Number of Elements: "))

for i in range(n):
	k = input("Enter Key: ")
	v = input("Enter Value: ")
	a.update({k:v})
	
print(a)