#!/usr/bin/python2

#import modeule
import socket
import os
import commands

#for make connection between sender and receiver
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#for binding the network 
s.bind(("127.0.0.1",7777))

for i in range(10000):
	#to get the data from sender side
	data = s.recvfrom(10000)
	#to get the status of input 
	check = commands.getstatusoutput(data[0])
	if check[0]==0:
		#if command found
		msg=os.system('echo "command found" | festival --tts')
		s.sendto(str(msg),data[1])
		
	else:
		#if command not found
		msg=os.system('echo "command not found" | festival --tts')
		s.sendto(str(msg),data[1])
