#!/usr/bin/python2
import  cgi
import commands

print("Content-type:text/html\n")
print(" ")

form = cgi.FieldStorage()
cname = form.getvalue('cname')
imgname = form.getvalue('imgname')
print("<html>")
print("<head>")
print("</head>")
print("<body bgcolor='#adadeb'></body>")
print("</html>")

#print(cname , imgname)

docker_launch_output =commands.getstatusoutput('sudo docker run -itd  --name {} -p   9998:4200  {}'.format(cname,imgname))
commands.getoutput('sudo docker exec {} service shellinaboxd start'.format(cname))

if docker_launch_output[0]  == 0:
	print('container named {} launched .. and Username is:root and Password is : q'.format(cname))
	print("<a href='http://192.168.43.142/cgi-bin/docker-manage.py'>click here to manage Container</a>")
else:
	
	print("container named {} failed ..".format(cname))

