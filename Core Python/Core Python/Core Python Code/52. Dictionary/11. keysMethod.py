# Dictionary - keys() Method
stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }
print("Original Dict:")
print(stu)
print()

all_keys = stu.keys()
print(all_keys)
print()
# converting into list
keys_lst = list(all_keys)
# printing converted list
print(keys_lst)
print()
# accessing one element
print(keys_lst[0])
print(keys_lst[1])
print(keys_lst[2])
print()
for k in keys_lst:
		print(k)