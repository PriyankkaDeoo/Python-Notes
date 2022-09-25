# Create Database
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
	
sql = 'CREATE DATABASE pdb'
myc = conn.cursor()
myc.execute(sql)
myc.close()
conn.close()
