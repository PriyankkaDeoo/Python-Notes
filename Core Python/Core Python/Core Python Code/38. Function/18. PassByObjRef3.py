# Pass/Call by Object Reference 
# Example 3
def val(lst):
	print("Inside Function Before New:", lst, id(lst))
	# Create New list object
	lst = [11, 22, 33]
	print("Inside Function After New:", lst, id(lst))
	
lst = [1, 2, 3]
print("Before Calling Func:", lst, id(lst))
val(lst)
print("After Calling Func:", lst, id(lst))

