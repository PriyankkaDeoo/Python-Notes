# Pass/Call by Object Reference 
def val(lst):
	print("Inside Function Before Append:", lst, id(lst))
	lst.append(4)
	print("Inside Function After Append:", lst, id(lst))
	
lst = [1, 2, 3]
print("Before Calling Func:", lst, id(lst))
val(lst)
print("After Calling Func:", lst, id(lst))

