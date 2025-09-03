#!/usr/bin/env python3
import cgi
#import sqlite3
import mysql.connector
import os

db = mysql.connector.connect(
    host=os.environ['DB_HOST'],
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'],
    database=os.environ['DB_DATABASE']
)

#conn = sqlite3.connect('/etc/httpd/db/clients.db')
curs = db.cursor()
print("Content-type:text/plain\n\n")
form = cgi.FieldStorage()
querystring = form.getvalue("querystring")

if querystring is not None:
    queryval = "%" + querystring + "%"
    select = "SELECT * FROM clients WHERE name LIKE '" + queryval + "'"
else:
    select = "SELECT * FROM clients"
curs.execute(select)
result = curs.fetchall()
for row in result:
    if len(row) == 4:
        for item in row:
            print(item,'|')
        print("#")
db.close()
