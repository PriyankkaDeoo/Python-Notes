# Dictionary - copy() Method
stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }
print("Original Dict:")
print(stu)
print(id(stu))
print()

new_stu = stu.copy()
print("Copied Dict:")
print(new_stu)
print(id(new_stu))