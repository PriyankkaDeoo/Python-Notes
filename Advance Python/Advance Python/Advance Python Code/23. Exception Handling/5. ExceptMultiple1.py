a = 10
b = 0
try:
    d = a/g
    print(d)
    
except ZeroDivisionError as obj:
    print(obj)
    
except NameError as ob:
    print(ob)

print('Rest of the Code')