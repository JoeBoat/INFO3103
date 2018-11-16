#!/bin/env python3
#
# Initial demonstration of pymysql to call a stored procedure
# Rick Wightman, September 2018
#
import pymysql.cursors
# Make the connection. Remember to fill in the string values for your credentials.
dbConnection = pymysql.connect('localhost',
					<userId>,
					<password>,
					<database_name>,
					charset='utf8mb4',
					cursorclass= pymysql.cursors.DictCursor)
sqlProcName = 'getSchools'

# Run query and get result
#### No error checking - this is a bad idea ####
cursor = dbConnection.cursor()
cursor.callproc(sqlProcName)
dbConnection.commit()
result = cursor.fetchone()
print(result)
print(cursor.fetchone() )
print(cursor.fetchone() )

#close dbConnection
dbConnection.close()
# End.
