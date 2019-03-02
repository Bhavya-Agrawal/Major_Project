#!/usr/bin/python2
import subprocess as sp
import cgi,commands
print("Content-type:text/html\n")
print(" ")
commands.getoutput("sudo systemctl restart  docker.service")
dockerImageList = commands.getoutput("sudo docker images")

dockerimage = dockerImageList.split("\n")
print("<html>")
print("<head><center><h1 style='color: #2e3347;font-size:230%;'>CAAS SERVICE</h1><center>")
print("</head>")
print("<body bgcolor='#adadeb'></body>")
print("</html>")
print("""
<form action='http://192.168.43.142/cgi-bin/CAAS_launch.py'>
<table align="center" width='80%' border='1' style='background-color:#cce0cc;'>
<tr>
<td>Enter Your Container Name :</td> 
<td><input name='cname' placeholder="Enter Container Name" required/></td>
</tr>

<tr>
<td>Enter Your Image Name :</td> 
<td>

<select name='imgname'>

""")


for i in dockerimage[1:] :
	print("<option>")
	j = i.split()
	print(j[0] + ":"  +  j[1])
	print("</option>")


print("""
</select>

</td>
</tr>

<tr>
<td><input type='submit'/></td> 
<td><input type='reset'/></td>
</tr>

</table>
</form>
""")
