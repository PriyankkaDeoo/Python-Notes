
def show(a,b):
	while a<=b :
		yield a
		a+=1

result = show(1, 5)
print(result)
print(type(result))
	
print(next(result))
print(next(result))
print(next(result))

for i in result:
	print(i)
