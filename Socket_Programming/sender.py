#!/usr/bin/python2

#import modeule
import socket

# to make connection between sender and receiver
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
'''
socket --- ip(4Byte)+port(2bytes) -- 6bytes
'''



for i in range(100000):
	     msg=raw_input("enter your msg :  ")
	     s.sendto(msg,("127.0.0.1",7777))			#To send message to receiver
	     s.recvfrom(1000)					#To print receive message in sender side
