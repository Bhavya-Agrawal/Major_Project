#!/usr/bin/python

import cgi,os,sys,time,commands

print "Content-Type: text/html\r\n\r\n"

z=cgi.FieldStorage()
f=z.getvalue('f')
v=z.getvalue('v')
c=z.getvalue('c')
w=z.getvalue('w')
s=z.getvalue('s')
o=z.getvalue('o')
g=z.getvalue('g')

if f=='f':
	print "<meta http-equiv='refresh' content='0; url=/firefox.sh'/>"
if v=='v':
	print "<meta http-equiv='refresh' content='0; url=/vlc.sh'/>"
if c=='c':
	print "<meta http-equiv='refresh' content='0; url=/cal.sh'/>"
if w=='w':
	print "<meta http-equiv='refresh' content='0; url=/webcam.sh'/>"
if s=='s':
	print "<meta http-equiv='refresh' content='0; url=/screenshot.sh'/>"
if o=='o':
	print "<meta http-equiv='refresh' content='0; url=/office.sh'/>"
if g=='g':
	print "<meta http-equiv='refresh' content='0; url=/gedit.sh'/>"
