# Delete Row From User Input - Tuple
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
	
sql = 'DELETE FROM student WHERE stuid=%s'
myc = conn.cursor()
n = int(input('Enter StuID: '))
del_value = (n,)
try:
	myc.execute(sql, del_value)
	conn.commit()		# Committing the change
	print(myc.rowcount, 'Row Deleted')
except:
	conn.rollback()		# Rollback the change
	print('Unable to Delete Data')
myc.close()		# Close Cursor
conn.close()	# Close Connection
