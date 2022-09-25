# Retrieve Row one by one
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
	
sql = 'SELECT * FROM student'
myc = conn.cursor()
try:
	myc.execute(sql)
	row = myc.fetchone()
	while row is not None:
		stuid = row[0]
		name = row[1]
		roll = row[2]
		fees = row[3]
		print(f'StuID: {stuid} Name: {name} Roll: {roll} Fees: {fees}')
		row = myc.fetchone()
	print('Total Rows:',myc.rowcount)
except:
	print('Unable to Retrieve Data')
myc.close()		# Close Cursor
conn.close()	# Close Connection
