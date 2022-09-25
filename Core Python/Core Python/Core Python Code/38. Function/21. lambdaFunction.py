# Anonymous Function or Lambda Function
#Example 1 Single Argument
show = lambda x : print(x)
show(5)

#Example 2 Two Arguments
add = lambda x,y : (x+y)
print(add(5, 2))

#Example 3 Return Multiple
add_sub = lambda x,y : (x+y, x-y)
a, s = add_sub(5, 2)
print(a)
print(s)

#Example 2 with Default Argument
add = lambda x,y=3 : (x+y)
print(add(5))



