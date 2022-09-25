# Insert Multiple Row - List of Tuples
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
	
sql = 'INSERT INTO student(name, roll, fees) VALUES(%s, %s, %s)'
myc = conn.cursor(prepared=True)
seq_of_params = [
	("Niti", 222, 30000.50),		# List of Tuples
	("Himesh", 333, 70000.50),
	("Arijit", 444, 50000.50)]
try:
	myc.executemany(sql, seq_of_params)
	conn.commit()		# Committing the change
	print(myc.rowcount, 'Row Inserted')		# Number of Row Inserted
except:
	conn.rollback()		# Rollback the change
	print('Unable to Insert Data')
myc.close()		# Close Cursor
conn.close()	# Close Connection


