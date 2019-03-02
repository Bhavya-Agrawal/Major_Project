#!/usr/bin/python2
import commands,cgi


print("Content-type:text/html\n")
print(" ")


#print("<iframe name='cframe' width='100%' height='25%'>container console</iframe>")

list = commands.getoutput("sudo docker ps -a")

flist = list.split("\n")
print("<html>")
print("<head><center><h1 style='color: #2e3347;font-size:230%;'>CONTAINER TABLE</h1><center>")
print("</head>")
print("<body bgcolor='#adadeb'></body>")
print("</html>")

print("<table align='center' width='90%' border='1'style='background-color:#cce0cc;'>")

print("""
<tr>
<th>Status</th>
<th>Image Name</th>
<th>Container Name</th>
<th>start</th>
<th>stop</th>
<th>Console</th>
</tr>
""")

for i in flist[1:]:
	j = i.split()
	print("<tr>")
	print("<td>")
	if "Exited" in i:
		print("down")
	elif "Up" in i:
		print("up")
	else:
		print("unknown")
	print("</td>")

	print("<td>")
	print(j[1])
	print("</td>")

	print("<td>")
	print(j[-1])
	print("</td>")

	print("<td>")
	print("<a href='docker-start.py?x={}'>start</a>".format(j[-1]))
	print("</td>")

	print("<td>")
	print("<a href='docker-stop.py?x={}'>stop</a>".format(j[-1]))
	print("</td>")


	print("<td>")
	print("<a href='http://192.168.43.142:9998'>console</a>")
	print("</td>")


	print("</tr>")


print("</table>")

