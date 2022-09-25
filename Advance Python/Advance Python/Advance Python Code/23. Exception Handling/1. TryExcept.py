#a = 10
#b = 0
#d = a/b
#print(d)
#print('Rest of the Code')

a = 10
b = 0
try:
    d = a/b
    print(d)
    print('Inside Try')
    
except ZeroDivisionError:
    print('Division by Zero Not allowed')
    
print('Rest of the Code')
