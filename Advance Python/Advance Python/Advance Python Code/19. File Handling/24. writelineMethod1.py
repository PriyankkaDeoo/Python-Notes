# Writing Data with w mode
f = open('student.txt', mode='w')
lst = ['Rahul', 'Sonam', 'Sumit', 'Rani', 'Raj']
f.writelines(lst)
f.close()
print('Success')