# Return Lambda Function
def add():
	y = 20
	return (lambda x : x+y)

a =add()
print(a(10))