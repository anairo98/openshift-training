#!/usr/bin/env python3
import os
import cgi
import requests
import socket

print("Content-type:text/html\n\n")
print("<head><title>Customer Database</title></head>\n")
print("<body>\n")
print("<h1>Customer Database Access</h1>\n")

api_host = os.getenv("API_HOST")
if ! api_host:
  print("Please provide API_HOST and API_PORT as environment variable!")
  exit(2)
api_port = os.environ["API_PORT"] if "DB_PORT" in os.environ.keys() else "8080"
if ! api_port:
  print("Please provide API_HOST and API_PORT as environment variable!")
  exit(2)

#remote = os.getenv("REMOTE_ADDR")
form = cgi.FieldStorage()
querystring = form.getvalue("querystring")
print(querystring)
print("___")
#if remote in webservers:
#    accessName = webservers[remote]
#else:
#    accessName = remote
accessName = socket.gethostname()

print("Accessed via Pod:", accessName, "\n<p>")

if querystring != None:
    url = 'http://'+api_host+':'+api_port+'/cgi-bin/data.py?querystring=' + querystring
else:
    url = 'http://'+api_host+':'+api_port+'/cgi-bin/data.py'
    querystring = ""

r = requests.get(url)

print('<form action="/cgi-bin/app.py">')
print(' Name Filter (blank for all records):')
print(' <input type="text" name="querystring" value="'+querystring+'">')
print(' <input type="submit" value="Apply">')
print('</form>')

print("\n<table border=1 bordercolor=black cellpadding=5 cellspacing=0>")

print("\n<th>Rank</th><th>Name</th><th>Universe</th><th>Revenue</th>")

# deal with the data coming across the wire
a = r.text.split("|\n#")
for row in a:
    if len(row) != 1:
        print("<tr>")
        splitrow = row.split("|")
        for item in splitrow:
            if item != None:
                print("<td>",item,"</td>")
        print("</tr>\n")
    print("</body></html>\n")
