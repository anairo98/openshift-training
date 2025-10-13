#!/usr/bin/env python3
import os
import cgi
import mysql.connector

db = mysql.connector.connect(
    host=os.environ['DB_HOST'],
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'],
    database=os.environ['DB_DATABASE']
)

form = cgi.FieldStorage()
rank = form["rank"].value
name = form["name"].value
universe = form["universe"].value
revenue = form["revenue"].value
print("Rank: "+str(rank)+" ("+str(type(rank))+")")
print("Name: "+str(name)+" ("+str(type(name))+")")
print("Universe: "+str(universe))
print("Revenue: "+str(revenue))
cursor = db.cursor()
add_command = ("INSERT INTO clients "
               "(Rank, Name, Universe, Revenue) "
               "VALUES (%s, %s, %s, %s)")

add_data = (rank, name, universe, revenue)

cursor.execute(add_command, add_data)

db.commit()

cursor.close()
db.close()
