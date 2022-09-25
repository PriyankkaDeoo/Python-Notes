# Passing Dictionary to Function
def show(d):
	print(d)
	print(type(d))
	for k in d:
		print(k,'=',d[k])

dc = {101:'Rahul', 102:'Raj', 103:'Sonam'}
show(dc)



