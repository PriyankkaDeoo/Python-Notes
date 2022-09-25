# Show Tables
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
	
sql = 'SHOW TABLES'
myc = conn.cursor()
myc.execute(sql)
for t in myc:
	print(t)
myc.close()
conn.close()
