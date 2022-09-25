#Default Arguments
#Example 1
def show(name, age):
	print(f"Name: {name} Age: {age}")
	
show(name="GeekyShows", age=62)

#Example 2
def show(name, age=27):
	print(f"Name: {name} Age: {age}")
	
show(name="GeekyShows")

#Example 3
def show(name, age=27):
	print(f"Name: {name} Age: {age}")
	
show(name="GeekyShows", age=62)

#Example 4 will show Error
#def show(name, age=27):
#	print(f"Name: {name} Age: {age}")
	
#show(name="GeekyShows", age=62, roll=101)
