# Insert Multiple Row
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
	
sql = 'INSERT INTO student(name, roll, fees) VALUES("Jai", 104, 40000.50), ("Veeru", 105, 50000.50), ("Basanti", 106, 60000.50)'
myc = conn.cursor()
try:
	myc.execute(sql)
	conn.commit()		# Committing the change
	print(myc.rowcount, 'Row Inserted')		# Number of Row Inserted
except:
	conn.rollback()		# Rollback the change
	print('Unable to Insert Data')
myc.close()		# Close Cursor
conn.close()	# Close Connection
