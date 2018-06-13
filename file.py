#!/usr/bin/python2

#import system-specific parameters and function
import sys


#to get only file name
f_name=sys.argv[1:]

for i in f_name:
	#a because if file already exist then can't change the existing data
	open(i,'a')
