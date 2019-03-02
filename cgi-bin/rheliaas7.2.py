#!/usr/bin/python2
import cgi
import os
import cgitb
import commands
import sys

cgitb.enable()
print "Content-type:text/html"

print ""

#taking data from apache server
data=cgi.FieldStorage()

# os Taking name as input
#sci=data.getvalue('s')
os_name=data.getvalue('osname')

#Taking os cpu as input
os_cpu=data.getvalue('oscpu')

#Taking os ram as input
os_ram=data.getvalue('osram')

#Taking port number as input
port_no=data.getvalue('portno')
#if sci=="1":
commands.getoutput('sudo qemu-img create -f qcow2 -b /var/lib/libvirt/images/rhvmdnd.qcow2 /var/lib/libvirt/images/{}.qcow2'.format(os_name))
	#print image
	#Installing the virtual os on the virtua manager
commands.getoutput('sudo virt-install --name {} --ram {} --vcpu {} --disk path=/var/lib/libvirt/images/{}.qcow2 --import --noautoconsole '.format(os_name,os_ram,os_cpu,os_name))
#print "Done"
print "<meta http-equiv='refresh' content='0; url=http://192.168.43.142/mainpage.html' />"


	#print install	
#else :
 #print "hello"
