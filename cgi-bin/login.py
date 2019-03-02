#!/usr/bin/python2
import mysql.connector 
import cgi
import os
import cgitb

cgitb.enable()
print "Content-type:text/html"

print ""
#taking data from apache server
data=cgi.FieldStorage()

Cemail=data.getvalue('email') 
Cpassword=data.getvalue('password')
    
con=mysql.connector.connect(user='root',password='123',host='localhost',database='project')   
sql_lang=con.cursor()
query="""select email,password from info"""
sql_lang.execute(query)
flag=0;
for email,password in sql_lang:
	if Cemail == email and Cpassword == password:
		flag=1;
		break;
	elif Cemail != email or Cpassword != password:
		flag=0;
if flag==1:
	print "<META HTTP-EQUIV='refresh' content='0; url=http://192.168.43.142/mainpage.html'>"

elif flag==0:
	print "<META HTTP-EQUIV='refresh' content='0; url=http://192.168.43.142/login.html'/>"	

