#!/bin/env python3
#
# Improved demonstration of pymysql to call a stored procedure
# Rick Wightman, September 2018
#
import pymysql.cursors
import settings
# Make the connection
dbConnection = pymysql.connect(settings.DBHOST,
					settings.DBUSER,
					settings.DBPASSWD,
					settings.DBDATABASE,
					charset='utf8mb4',
					cursorclass= pymysql.cursors.DictCursor)
sqlProcName = 'getSchools'

# Run query and get result
try:
	cursor = dbConnection.cursor()
	cursor.callproc(sqlProcName)
	dbConnection.commit()

	# We get all of the results and then iterate through them.
	results = cursor.fetchall()

	# ACK - It's C revisited!
	for row in results:
		print ("%s, %s" % (row["name"], row["province"]) )

except pymysql.MySQLError as e:
	# failure
	print(e)
finally:
	#close dbConnection
	dbConnection.close()

# End.
