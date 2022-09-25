# Retrieve Single Row - Input From User - Tuple
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
	
sql = 'SELECT * FROM student WHERE stuid=?'
myc = conn.cursor(prepared=True)
n = int(input('Enter StuID to Display: '))
disp_value = (n,)
try:
	myc.execute(sql, disp_value)
	row = myc.fetchone()
	print(row)
	print('Total Rows:',myc.rowcount)
except:
	print('Unable to Retrieve Data')
myc.close()		# Close Cursor
conn.close()	# Close Connection
