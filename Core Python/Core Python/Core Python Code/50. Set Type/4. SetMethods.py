# Set Methods

a = {'Rahul', 'Raj', 'Sonam', 'Rani'}
b = {'Sumit', 'Rahul', 'Rani', 'Python', 'Java'}

print("A:",a)
print("B:",b)
print()

# intersection() Method
	# returns item which exists in both sets
ism = a.intersection(b)
print("Intersection:", ism)
print()

# union() Method
	# Returns all item from original set and all items from specified set
um = a.union(b)
print("Union:", um)
print()

# difference() Method
	# Returns items that exist only in first set, and not in both sets
dm = a.difference(b)
print("Difference:", dm)
print()

# issubset() Method
	#Returns True if all items in the set exists in the specified set
isub = a.issubset(b)
print("issubset:", isub)
print()

# issuperset() Method
  # Returns True if all items in the specified set exists in the original set
isup = a.issuperset(b)
print("issuperset:", isup)
print()