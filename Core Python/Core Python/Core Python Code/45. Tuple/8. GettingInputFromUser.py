# Getting input from users - Tuple
a = []

n = int(input("Enter Number of Elements: "))

for i in range(n):
	a.append(int(input("Enter Element:")))

print(type(a))
# convert list to tuple 
a = tuple(a)

print(type(a))
print("Tuple:")
for element in a:
	print(element)
