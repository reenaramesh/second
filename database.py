"""import MySQLdb
import sys

# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
connection = MySQLdb.connect (host = "192.168.6.248", user = "root", password = "asm123", db = "book")

# prepare a cursor object using cursor() method
cursor = connection.cursor ()

# execute the SQL query using execute() method.
cursor.execute ("name, publish")

# fetch all of the rows from the query
data = cursor.fetchall ()

# print the rows
for row in data :
 print row[0], row[1]

# close the cursor object
 cursor.close ()

# close the connection
 connection.close ()

# exit the program
 sys.exit()


import MySQLdb


# Open database connection ( If database is not created don't give dbname)
db = MySQLdb.connect("localhost","asm","asm123","school" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# For creating create db
# Below line  is hide your warning
cursor.execute("SET sql_notes = 0; ")
# create db here....
cursor.execute("create database IF NOT EXISTS school")



# create table
cursor.execute("SET sql_notes = 0; ")
cursor.execute("create table IF NOT EXISTS details( name varchar(25),  publisher varchar(12));")
cursor.execute("SET sql_notes = 1; ")

#insert data
cursor.execute("insert into school(name,publisher) values('something','asm')")

# Commit your changes in the database
db.commit()

# disconnect from server
db.close()"""

import re
"""import MySQLdb

db = MySQLdb.connect(host="localhost",  # your host
                     user="root",  # username
                     passwd="asm123",  # password
                     db="book")  # name of the database

# Create a Cursor object to execute queries.
cur = db.cursor()

#cur.execute("create database student")

# Select data from table using SQL query.
#cur.execute("SELECT * FROM details")

# print the first and second columns
#for row in cur.fetchall():
#    print row[0], " ", row[1]"""




import re

file1 = open("/home/asm/Downloads/diag.out", "r ")
l1 = []

for line in file1:
	str1 = re.match("----- APmgr info: apmgrinfo -a", line, re.M|re.I)
	if str1:
		for lines in file1:
			l1.append(lines)
			str2 = re.match("----- Disconnected APs: wlaninfo --all-disc-ap -l 3", lines, re.M|re.I)
			if str2:
				break

#for i in l1:
#	print i


l2 = []
for x in l1:
    if x == "":
    #s1 = re.match("Model/Serial Num ", x, re.M|re.I)
    #if s1:
        #for x in l1:
            l2.append(x)
#for y in l2:
 #print x
mac = []
for i in l1:
    m = re.search(r'[a-fA-F0-9]{2}[:][a-fA-F0-9]{2}[:][a-fA-F0-9]{2}[:][a-fA-F0-9]{2}[:][a-fA-F0-9]{2}[:][a-fA-F0-9]{2}', i)
    if m:

        print "MAC Address :\t", m.group()
for i in l1:
    ip = re.search('(([2][5][0-5]\.)|([2][0-4][0-9]\.)|([0-1]?[0-9]?[0-9]\.)){3}'
                +'(([2][5][0-5])|([2][0-4][0-9])|([0-1]?[0-9]?[0-9]))', i)
    if ip:
	    print " ip address:\t"  , ip.group()

for i in l1:
 patt = re.search('''^([2][0-5][0-5]|^[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})$''', i)
 if patt:
		print " ipv4 address:\t"  , patt.group()

for i in l1:
	name =  re.search('[A-ZA-Z0-90-90-90-90-9][-]',i)
	if name:
		 print "name:\t", name.group()
#re.search('([A-H][A-Z][0-9][0-9][0-9][0-9][0-9])' + '([W-Z][A-Z][0-9][0-9][0-9][0-9])', i)

