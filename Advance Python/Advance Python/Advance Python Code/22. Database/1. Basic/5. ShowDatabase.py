# Show Database
import mysql.connector
try:
	conn= mysql.connector.connect(
		user='root', 
		password='geek', 
		host='localhost', 
		port=3306
	)
	if (conn.is_connected()):
		print('Connected')
except:
	print('Unable to Connect')
	
sql = 'SHOW DATABASES'
myc = conn.cursor()
myc.execute(sql)
for d in myc:
	print(d)
myc.close()	
conn.close()
