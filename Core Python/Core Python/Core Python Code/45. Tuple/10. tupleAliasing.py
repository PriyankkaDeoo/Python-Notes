a = (10, 20, 30, 40, 50)
b = a
print("A:", a)
print("B:", b)
print("Id of A:", id(a))
print("Id of B:", id(b))

print()
a = a[:3]
print("Id of A:", id(a))
print("Id of B:", id(b))