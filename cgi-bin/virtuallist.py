#!/usr/bin/python2
import commands,cgi



print("Content-type:text/html\n")
print(" ")

print ("<html>")
print("<head><center><h1 style='color: #2e3347;font-size:230%;'>VIRTUAL LIST</h1><center>")
#print("<style>")
'''
#print(".bg-img { background-image:"win.jpg";min-height: 900px;background-position: center;background-repeat: no-repeat;background-size: cover;")
#print("body {background-image: url("https://i.pinimg.com/originals/19/57/a4/1957a42f33fa8b5c543527213f580c3c.jpg");background-size: 100% 110%;}")
#print("<img src = 'login.jpg' height = '400' width = '500'>")

'''
#print("</style>")
print("</head>")
print("<body bgcolor=' #adadeb'></body>")

print("</html>")

#print("<iframe name='cframe' width='100%' height='25%'>container console</iframe>")

list = commands.getoutput("sudo virsh list --all")

flist = list.split("\n")


print("<table align='center' width='90%' border='1' style='background-color:lightgrey;'>")

print("""
<tr style='background-color:#eb9999;'>
<th>State</th>
<th>Name</th>

</tr>
""")

for i in flist[2:]:
	j = i.split()
	
	print("<tr>")
	
	print("<td>")
	if "shut" in i:
		print("down")
	elif "running" in i:
		print("up")
	else:
		print("unknown")
	print("</td>")
	
	print("<td>")
	print(j[1])
	print("</td>")
	'''
	print("<td>")
	print(j[2])
	print("</td>")
	'''
	'''
	print("<td>")
	print("<a href='virtualstart.py?x={}'>start</a>".format(j[1]))
	print("</td>")

	print("<td>")
	print("<a href='virtualoff.py?x={}'>stop</a>".format(j[-1]))
	print("</td>")
	print("</tr>")
	'''


print("</table>")

