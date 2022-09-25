# Update Row - Dictionary
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
	
sql = 'UPDATE student SET fees=%(fee)s WHERE stuid=%(id)s'
myc = conn.cursor()
update_value = {'fee':500, 'id':9}
try:
	myc.execute(sql, update_value)
	conn.commit()		# Committing the change
	print(myc.rowcount, 'Row Updated')
except:
	conn.rollback()		# Rollback the change
	print('Unable to Update Data')
myc.close()		# Close Cursor
conn.close()	# Close Connection
