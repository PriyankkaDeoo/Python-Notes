# Getting input from user
# Empty Set
a = set()
print(id(a))
n = int(input("Enter number of Elements: "))

for i in range(n):
	el = input("Enter Element: ")
	a.add(el)

# Accessing set 
for i in a:
	print(i)

print(id(a))
