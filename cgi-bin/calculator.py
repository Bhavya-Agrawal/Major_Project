import socket,os,sys,commands,time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sip="192.168.43.142"
s_port=8888

os.system("SSHPASS='123' sshpass -e ssh -X deeksha@"+sip+" gnome-calculator")


execfile('SAAS.py')
