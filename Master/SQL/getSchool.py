#!/bin/env python3
#
# Improved demonstration of pymysql to call a stored procedure
# Rick Wightman, September 2018
#
import pymysql.cursors
import settings
# Make the connection. The settings.py file holds the credentials.
dbConnection = pymysql.connect(settings.DBHOST,
					settings.DBUSER,
					settings.DBPASSWD,
					settings.DBDATABASE,
					charset='utf8mb4',
					cursorclass= pymysql.cursors.DictCursor)
sqlProcName = 'getSchools'

# Run query and get result. Notice we check for problems.
try:
	cursor = dbConnection.cursor()
	cursor.callproc(sqlProcName)
	dbConnection.commit()
	result = cursor.fetchone()
	print(result)
	print(cursor.fetchone() )
	print(cursor.fetchone() )
except pymysql.MySQLError as e:
	# failure
	print(e)
finally:
	#close dbConnection
	dbConnection.close()

# End.
