# Dictionary - pop() Method
stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }
print("Original Dict:")
print(stu)
print(id(stu))
print()

removed_value = stu.pop(102)
#removed_value = stu.pop(106)	# Key is not found so KeyError
print("After Removing Dict:")
print(stu)
print(id(stu))
print("Removed Value:", removed_value)
print()

default_value = stu.pop(106, 'GeekyShows')
print("After Removing Dict:")
print(stu)
print(id(stu))
print("Default Value:", default_value)
print()

