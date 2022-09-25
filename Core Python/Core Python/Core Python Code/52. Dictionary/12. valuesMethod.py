# Dictionary - values() Method
stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }
print("Original Dict:")
print(stu)
print()

all_values = stu.values()
print(all_values)
print()
# converting into list
values_lst = list(all_values)
# printing converted list
print(values_lst)
print()
# accessing one element
print(values_lst[0])
print(values_lst[1])
print(values_lst[2])
print()
for v in values_lst:
		print(v)