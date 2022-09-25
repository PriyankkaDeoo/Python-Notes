# Insert Single Row - Input from User - Dictionary
import mysql.connector
try:
	conn= mysql.connector.connect(
		user='root', 
		password='geek', 
		host='localhost', 
		database='pdb',
		port=3306
	)
	if (conn.is_connected()):
		print('Connected')
except:
	print('Unable to Connect')
	
sql = 'INSERT INTO student(name, roll, fees) VALUES(%(name)s, %(roll)s, %(fees)s)'
myc = conn.cursor()
# Data from user
nm = input('Enter Name: ')
ro = int(input('Enter Roll: '))
fe = float(input('Enter Fees: '))
params =  {'name':nm, 'roll':ro, 'fees': fe}
try:
	myc.execute(sql, params)
	conn.commit()		# Committing the change
	print(myc.rowcount, 'Row Inserted')		# Number of Row Inserted
	print(f'Stu ID: {myc.lastrowid} Inserted')	# Last inserted ID
except:
	conn.rollback()		# Rollback the change
	print('Unable to Insert Data')
myc.close()		# Close Cursor
conn.close()	# Close Connection
