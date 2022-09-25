# Dictionary - items() Method
stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }
print("Original Dict:")
print(stu)
print()

it = stu.items()
print(it)
print()
# converting into list
lst = list(it)
# printing converted list
print(lst)
print()
# accessing one element
print(lst[0])
print(lst[0][0])
print(lst[0][1])
print()
for r in lst:
	for c in r:
		print(c)