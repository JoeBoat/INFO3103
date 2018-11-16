#!/bin/env python3
#
# getSchoolsWeb.py - Rick Wightman, modified September, 2017
#
# Example python script to access a database and return the data as a traditional web page
#
import pymysql.cursors
import settings
import cgitb
import cgi
import sys
cgitb.enable()

# Make the connection
dbConnection = pymysql.connect(settings.DBHOST,
                                        settings.DBUSER,
                                        settings.DBPASSWD,
                                        settings.DBDATABASE,
                                        charset='utf8mb4',
                                        cursorclass= pymysql.cursors.DictCursor)

sql = "getSchools"
# http headers
print ('Content-type: text/html')
print ()

# Run query and get result

print('<!DOCTYPE html>')
print('<head>\n\t<title>getSchoolsWeb</title>\n\t<meta charset="utf-8">\n</head>')
print('<body>')
print('<table>')
try:
        cursor = dbConnection.cursor()
        cursor.callproc(sql)
        results = cursor.fetchall()
        print('<tr><th>School Name</th><th>Province</th></tr>')
        for row in results:
                print("<tr><td> {name}</td><td>{province}</td></tr>".format(**row) )
        #       print('<tr><td>'+row['name']+'</td><td>'+row['province']+'</td></tr>' )

        print('</table>')
except pymysql.MySQLError as e:
        print('<p>Ooops - Things messed up: </p>')
except Exception as e:
        print('<p>Something big went wrong.</p>')
        print(e)

print('</body>\n</html>')

cursor.close()
dbConnection.close()

#End
