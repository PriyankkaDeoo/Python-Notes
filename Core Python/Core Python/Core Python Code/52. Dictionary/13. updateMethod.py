# Dictionary - update() Method
stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }
print("Original Dict:")
print(stu)
print(id(stu))
print()

stu.update({104: 'Python'})
print("Updated Dict:")
print(stu)
print(id(stu))
print()

vals = {'name': 'Rahul', 'Address': 'Ranchi', 105: 'GeekyShows'}
stu.update(vals)
print("Updated Dict:")
print(stu)
print(id(stu))
print()
