import os
w = os.walk('.')
for i in w:
	print(i)
print()

w = os.walk('yourdir')
for i in w:
	print(i)
print()

w = os.walk('yourdir', topdown=False)
for i in w:
	print(i)

