# Writing Data with a mode
f = open('student.txt', mode='a')
lst = ['Rahul\n', 'Sonam\n', 'Sumit\n', 'Rani\n', 'Raj\n']
f.writelines(lst)
f.close()
print('Success')

