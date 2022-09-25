# Creating Connection
import mysql.connector
config = {
	'user': 'root',
	'password': 'geek',
	'host': 'localhost',
	'port': 3306
}
try:
	conn= mysql.connector.connect(**config)
	if (conn.is_connected()):
		print('Connected')
except:
	print('Unable to Connect')

	

