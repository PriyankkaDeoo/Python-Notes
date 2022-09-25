# Insert Multiple Row - List of Dictionaries
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
seq_of_params = [										# List of Dictionaries
	{'name':'Ajay', 'roll':124, 'fees': 5426.23},		
	{'name':'Rani', 'roll':845, 'fees': 845621.23},
	{'name':'Rohit', 'roll':659, 'fees': 47426.23} ]
try:
	myc.executemany(sql, seq_of_params)
	conn.commit()		# Committing the change
	print(myc.rowcount, 'Row Inserted')		# Number of Row Inserted
except:
	conn.rollback()		# Rollback the change
	print('Unable to Insert Data')
myc.close()		# Close Cursor
conn.close()	# Close Connection
