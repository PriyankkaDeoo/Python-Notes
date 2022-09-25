# Thousand Separator
price = 1234567890
print(f"{price:,}")
print(f"{price:_}")

#Variable
name = "Rahul"
age= 62
print(f"My name is {name} and age {age}")

# Expression
print(f"{10*8}")

# Expressing a Percentage
a = 50
b = 3
print(f"{a/b:.2%}")

# Accessing arguments’ items
value = (10, 20)
print(f"{value[0]} {value[1]}")

# Format with Dict
data = {'rahul': 2000, 'sonam': 3000}
print(f"{data['rahul']:d} {data['sonam']:d}")

# Calling Function
name= "GeekyShows"
print(f"{name}")
print(f"{name.upper()}")

# Using object created from class
#print(f"{obj.name}")

# Curly Braces
print(f"{10}")
print(f"{{10}}")

# Date and Time
from datetime import datetime
today = datetime(2019, 10, 5)
print(f"{today}")
print(f"{today:%d-%b-%Y}")
print(f"{today:%d/%b/%Y}")
print(f"{today:%b/%d/%Y}")

# Datetime Directive https://docs.python.org/3.7/library/datetime.html#strftime-and-strptime-behavior

