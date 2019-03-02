#!/usr/bin/python2
import cgi,os,commands
print "Content-type:text/html\n"
print ""
web=cgi.FieldStorage()
p=web.getvalue('p')

'''if p=='python':
	commands.getoutput('sudo systemctl start docker.service')
	#commands.getoutput('sudo docker start 679b74c36c05')
	#commands.getoutput('sudo docker exec -it 679b74c36c05  /usr/bin/python')
	#commands.getoutput('sudo systemctl restart shellinaboxd')
	#commands.getoutput('sudo docker run -itd --name caas 4200:4200 caas')
	#commands.getoutput('sudo docker start caas')
	#commands.getoutput('sudo systemctl restart shellinaboxd')
	commands.getoutput('sudo docker run  -itd --name caas -p 9799:4200 caas')
	commands.getoutput('sudo docker start caas')
	commands.getoutput('sudo exec caas service shellinaboxd start')
	print "<a href='https://192.168.43.142:4200'>"
	print "Username is deeksha and password is redhat"
	print "</a>"'''

commands.getoutput('sudo systemctl start docker.service')
if p=='python' :
	'''commands.getoutput('sudo docker start 44d32cda8f4c')
	commands.getoutput('sudo docker attach 44d32cda8f4c')
	x=commands.getoutput('sudo docker exec -it 44d32cda8f4c /usr/bin/python')
	commands.getstatusoutput('sudo systemctl restart shellinaboxd')'''
	commands.getoutput('sudo docker run -itd --name paas -p 4200:4200 centos6:paas')
	commands.getoutput('sudo docker start paas')
	print "<a href='https://192.168.43.142:4200'>"
        print "Username is code and password is code"
        print "</a>"
elif p=='perl' :
	commands.getoutput('sudo docker run  -itd --name caas -p 9799:4200 caas')
        commands.getoutput('sudo docker start caas')
        commands.getoutput('sudo exec caas service shellinaboxd start')
        print "<a href='https://192.168.43.142:4200'>"
        print "Username is deeksha and password is redhat"
        print "</a>"
elif p=='java' :
	commands.getoutput('sudo docker run  -itd --name caas -p 9799:4200 caas')
        commands.getoutput('sudo docker start caas')
        commands.getoutput('sudo exec caas service shellinaboxd start')
        print "<a href='https://192.168.43.142:4200'>"
        print "Username is deeksha and password is redhat"
        print "</a>"
