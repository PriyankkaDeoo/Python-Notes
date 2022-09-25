# Deletion

stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }
print("Before Deletion:")
print(stu)
print(id(stu))
print()

del stu[102]
print("After Deletion:")
print(stu)
print(id(stu))
print()

# Delete Entire Dictionary
del stu

print(stu)		# It will show error stu not defined



