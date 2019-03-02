#!usr/bin/python

import os,time,socket,getpass


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s_ip="192.168.43.142"
s_port=8888


#os.system('sshpass -p "q" ssh -X a@'+s_ip+' office' + ' &>/dev/null')
os.system('sshpass -p "redhat" ssh -X  deeksha@'+s_ip+' office' )
