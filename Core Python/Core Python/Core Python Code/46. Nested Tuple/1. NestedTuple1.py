# Nested Tuple
# Example 1
a = (10, 20, 30, (50, 60))
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[3][0])
print(a[3][1])
print()
# Example 2
b = (50, 60)
a = (10, 20, 30, b)
print("A:",a)
print("B:",b)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[3][0])
print(a[3][1])


