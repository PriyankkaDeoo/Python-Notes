a = 10
b = 5
try:
    d = a/b
    print(d)
    print('Inside Try')
    
except ZeroDivisionError:
    print('Division by Zero Not allowed')
    
else:
    print('Inside Else')
    
print('Rest of the Code')