# Dictionary - popitem() Method
stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }
print("Original Dict:")
print(stu)
print(id(stu))
print()

removed_item = stu.popitem()
print("After Removing Dict:")
print(stu)
print(id(stu))
print("Removed Value:", removed_item)
print()



