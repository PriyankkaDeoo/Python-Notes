# Sets - copy() Method

a = {10, 20, 'GeekyShows'}
print("Before Copy",a)
print(id(a))
print()

new_a = a.copy()

print("After Copy", new_a)
print(id(new_a))
