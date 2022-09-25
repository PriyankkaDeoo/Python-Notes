a = 10
b = 0
try:
    d = a/b
    print(d)
    print('Inside Try')
    
except ZeroDivisionError as obj:
    print(obj)

print('Rest of the Code')