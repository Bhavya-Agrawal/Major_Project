#!/usr/bin/python2
import os,cgi,commands
print "Content-type:text/html\n"
print ""
web=cgi.FieldStorage()
ds=web.getvalue('ds')
#j=commands.getstatusoutput('sudo yum install scsi-target-utils-gluster.x86_64')
commands.getoutput('sudo systemctl restart tgtd')
a="<target hello>\nbacking-store  "+ds+"\n</target>"
f=open('/etc/tgt/targets.conf','a')
f.write(a)
f.close()
