# Retrieve Number of Rows
import mysql.connector
conn= mysql.connector.connect(
	user='root', 
	password='geek', 
	host='localhost', 
	database='pdb',
	port=3306
)
if (conn.is_connected()):
	print('Connected')
	
sql = 'SELECT * FROM student'
myc = conn.cursor(buffered=True)
myc.execute(sql)
rows = myc.fetchmany(size=5)
for row in rows:
	print(row)
print('Total Rows:',myc.rowcount)
myc.close()		# Close Cursor
conn.close()	# Close Connection
