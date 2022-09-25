# Recursion
# Example 1
i = 0
def myfun():
	global i
	i+=1
	print("My Function", i)
	myfun()
	
myfun()

# Example 2
import sys
# get recursion limit
print("Default:",sys.getrecursionlimit())

# set recursion limit
sys.setrecursionlimit(3000)

print("After setting:", sys.getrecursionlimit())
