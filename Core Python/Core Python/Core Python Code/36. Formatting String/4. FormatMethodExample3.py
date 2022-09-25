# Comma as thousand Separator
print("{:,}".format(1234567890))

#variable
name = "Rahul"
age= 62
print("My name is {} and age {}".format(name, age))

# Expressing a Percentage
a = 50
b = 3
print("{:.2%}".format(a/b))

# Accessing arguments’ items
value = (10, 20)
print("{0[0]} {0[1]}".format(value))

# Format with Dict
data1 = {'rahul': 2000, 'sonam': 3000}
print("{0[rahul]:d} {0[sonam]:d}".format(data1))

# Format with Dict
data2 = {'rahul': 2000, 'sonam': 3000}
print("{d[rahul]:d} {d[sonam]:d}".format(d=data2))

# Accessing arguments by name:
data3 = {'rahul': 2000, 'sonam': 3000}
print("{rahul} {sonam}".format(**data3))	

# ** is a format parameter (minimum field width)