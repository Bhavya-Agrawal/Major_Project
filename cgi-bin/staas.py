#!/usr/bin/python2
import os,cgi,commands
g=raw_input()
x1=commands.getoutput('hostname -I')
ip=x1.split(' ')
nfs_write="/mnt/"+g+"    *(rw,no_root_squash)\n"

x=open('/etc/exports','a')
x.write(nfs_write)
x.close()

commands.getoutput('sudo exportfs -r')
commands.getoutput('sudo touch /mnt/projectx/deeksha1 > deeksha1.sh') 
m='deeksha1.sh'

commands.getstatusoutput("echo 'mkdir /mnt/deeksha1' > deeksha1.sh")
commands.getstatusoutput("echo mount {}:/mnt/deeksha1 /mnt/deeksha1 >> deeksha1.sh".format(ip[0]))

commands.getstatusoutput('sudo chmod o+w {}'.format(m))
commands.getstatusoutput('sudo chmod +x deeksha1.sh')
commands.getoutput('sudo tar cvf ../html/deeksha1.tar deeksha1.sh')
commands.getoutput('sudo cd /etc/fstab/'+'echo 192.168.122.1:mnt/deeksha1   swap                    swap    defaults        ')
