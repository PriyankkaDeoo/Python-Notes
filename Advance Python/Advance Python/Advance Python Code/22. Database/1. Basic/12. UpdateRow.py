# Update Row
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
	
sql = 'UPDATE student SET fees=200 WHERE stuid=4'
myc = conn.cursor()
try:
	myc.execute(sql)
	conn.commit()		# Committing the change
	print(myc.rowcount, 'Row Updated')
except:
	conn.rollback()		# Rollback the change
	print('Unable to Update Data')
myc.close()		# Close Cursor
conn.close()	# Close Connection
