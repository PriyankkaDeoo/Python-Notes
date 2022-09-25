# Passing Lambda Function to Another Function
def show(a):
	print(a)
	print(a(8))

show(lambda x: x)
