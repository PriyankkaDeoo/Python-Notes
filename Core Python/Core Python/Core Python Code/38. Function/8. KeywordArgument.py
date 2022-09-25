#Keyword Arguments
#Example 1
def show(name, age):
	print(f"Name: {name} Age: {age}")
	
show(name="GeekyShows", age=62)

#Example 2
def show(name, age):
	print(f"Name: {name} Age: {age}")
	
show(age=62, name="GeekyShows")

#Example 3 will show Error
#def show(name, age):
#	print(f"Name: {name} Age: {age}")
	
#show(name="GeekyShows", age=62, roll=101)
