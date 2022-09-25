# Retrieve All Rows with formatted output
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
	rows = myc.fetchall()
	for r in rows:
		stuid = r[0]
		name = r[1]
		roll = r[2]
		fees = r[3]
		print(f'StuID: {stuid} Name: {name} Roll: {roll} Fees: {fees}')
	print('Total Rows:',myc.rowcount)
except:
	print('Unable to Retrieve Data')
myc.close()		# Close Cursor
conn.close()	# Close Connection
