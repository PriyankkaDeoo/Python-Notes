# Dictionary - setdefault() Method
stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }
print("Original Dict:")
print(stu)
print(id(stu))
print()

#returned_value = stu.setdefault(102)
returned_value = stu.setdefault(109, 'Rohit')
print("After Set Default Dict:")
print(stu)
print(id(stu))
print("returned Value:", returned_value)
print()



