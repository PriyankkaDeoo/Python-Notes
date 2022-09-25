a = 10
b = 0
try:
    d = a/g
    print(d)
    
except (NameError, ZeroDivisionError) as obj:
    print(obj)

print('Rest of the Code')
