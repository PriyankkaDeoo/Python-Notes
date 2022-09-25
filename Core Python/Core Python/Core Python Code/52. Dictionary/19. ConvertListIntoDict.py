# Converting Lists into Dictionary
roll = [101, 102, 103]
name = ['Rahul', 'Raj', 'Sonam']

# make a dictionary
z = zip(roll, name)
d = dict(z)

for k in d:
	print(k,'=',d[k])