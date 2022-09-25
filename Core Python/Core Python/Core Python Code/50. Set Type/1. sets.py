# Sets

#Creating Empty Set
x = set()

#Cretaing Set with elements
a = {10, 20, 'GeekyShows', 'Raj', 40}

# Cant access using index
# print(a[0])		# It will show error
print(a)
print(id(a))
print()

# Duplicates are avoided
b = {10, 20, 'GeekyShows', 'Raj', 40, 10, 10}
print(b)
print()

# Adding one Element
print("Adding one Element:")
a.add('Python')
print(a)
print(id(a))
print()

#Adding Multiple Elements
print("Adding Multiple Element:")
a.update([101, 102, 103])
print(a)
print(id(a))
print()

#Deleting Element using discard() method
print("Removing Element using discard:")
a.discard('GeekyShows')
print(a)
print(id(a))
print()

#Deleting Element using remove() method
print("Removing Element using remove:")
a.remove('Raj')
print(a)
print(id(a))
print()


