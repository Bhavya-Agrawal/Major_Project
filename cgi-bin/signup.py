#!/usr/bin/python2


import cgi
import cgitb
import os
import mysql.connector


cgitb.enable()
print "Content-type:text/html"

print ""

#taking data from apache server
data=cgi.FieldStorage()

#taking email address entered by user
email=data.getvalue('mail')

#taking username entered by user
username=data.getvalue('uname')

#taking password entered by user
password=data.getvalue('psw')

#validate password entered by user
retype_psw=data.getvalue('psw-repeat')

#use database signup to store the information entered by user
con=mysql.connector.connect(user='root',password='123',host='localhost',database='project')

sql_lang=con.cursor()

for email in sql_lang:
	if email==email:
		print "email already exist"

if password==retype_psw:
	#storing the information of user into the schema
	sql_lang.execute("insert into info(email,username,password,retype) values('"+email+"','"+username+"','"+password+"','"+retype_psw+"');")
	print "<META HTTP-EQUIV='refresh' content='0; url=http://192.168.43.142/login.html'/>"

else:

	print "Enter same password"

#reflect changes into schema
con.commit()

sql_lang.close()
con.close()
