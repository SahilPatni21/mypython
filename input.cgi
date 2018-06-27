#!/usr/bin/python2

import commands
import cgi,time
#import cgitb

#cgitb.enable()

print "Content-Type:text/html"
print ""

data=cgi.FieldStorage()

command=data.getvalue('c')

if command == "ftp":
	print"executing..."
	time.sleep(2)
	print "<pre>"
	print commands.getoutput('yum install ftp')
	print "</pre>"

elif command == "ram":
        print"executing..."
        time.sleep(2)
        print "<pre>"
        print commands.getoutput('sudo free -m ')
	print "</pre>"

elif command == "time":
        print"executing..."
        time.sleep(2)
        print "<pre>"
        print commands.getoutput('date')
        print "</pre>"

elif command == "reboot":
        print"executing..."
        time.sleep(2)
        print "<pre>"
        print commands.getoutput('reboot')
        print "</pre>"

elif command == "cal":
        print"executing..."
        time.sleep(2)
        print "<pre>"
        print commands.getoutput('cal')
        print "</pre>"
