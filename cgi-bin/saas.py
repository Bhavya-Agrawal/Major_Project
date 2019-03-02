import os,time,commands,sys,socket

x="""
Press 1 to get Firefox  :
Press 2 to get vlc      :
Press 3 to open calculator:
Press 4 to open office   :
Press 5 to take a screenshot  :
Press 6 to to start the webcam      :
"""
print x

ch=raw_input()

if ch=='1':
	print "Now wait for a second"
	execfile('calculator.py')
else :
	print"FuckOff"

