#! /usr/bin/python2

import time                         #library to access time
import os                           #library for accessing the operating system
import webbrowser                   #library for opening the web browser
import facebook                     #library use to get access of facebook
import urllib                       #library for getting url from google
import requests                     #to send organic,grass-fed HTTP/1.1	
from bs4 import BeautifulSoup       #to wrap the url

#declaring a variable for the values to press the particular number to get access for the operation
x='''
Press 1 : to show current time :
Press 2 : to reboot OS :
Press 3 : to create a user in your current OS :
Press 4 : to search something on Google :
Press 5 : to search your data on google but print URL of first page
Press 6 : to check CPU and RAM info
Press 7 : to login your fb account and update status HELLO WORLD
Press 8 : to scan all the IP and MAC address in your network
'''


print x                                               #print option to user

choice = int(raw_input("Enter your choice Here:"))

if choice==1 :
	print "Showing current time: "
	print time.ctime().split()[3]                #to get current time         


elif choice == 2: 
	print "System is rebooting....."
        os.system('reboot')                          #to reboot the system


elif choice ==3:

        un=raw_input("Add Username: ")		    #getting input new user 
	up=raw_input("Add Password: ")		    #getting input password for the new user
        os.system('useradd '+un)                    #to get a new user
	os.system('passwd '+un)                     #to set a password for the user


elif choice ==4:
	x=raw_input("Enter your text here to search on Google: ")
	webbrowser.open_new_tab('http://www.google.com/search?q='+x)         #to open web browser

elif choice ==5:
	text = raw_input("enter your search")
	text = urllib.quote_plus(text)

	url = 'https://google.com/search?q=' + text
	
	response = requests.get(url)                                        #to get response from the url

	soup = BeautifulSoup(response.text, 'lxml')			    #to wrap the url

	for g in soup.find_all(class_='g'):
		
    		print(g.text)						     #to print url
    		print('-----')

	

elif choice ==6:
	print "Showing CPU and RAM info: "          
	os.system('free -m')                                                 #to get the processing of CPU and storage used by RAM


elif choice == 7:
	
	graph = facebook.GraphAPI('EAACEdEose0cBAC3g1n0dOCE6ZB751vc1gzXqvkJxHjtwFybaZAs27UNwUYOwPptusbkjlFLTU3zX7H9pCZBg5XrcUkuQ2CEcn7EROIxf6QmWrx0IKuXBBc9AH5jneKhZCblYZC9xKM3Pib4FzavhpECqm5QhPDCDLrGDgWoPJQvH7fWrJFCXGWerLgXDla1SaBiXdzvM8WwZDZD',version="2.12")						
	
	
	status=raw_input("enter your status: ")                                        #to get access of user_access_token for facebook and googleApi

	graph.put_object(parent_object='me', connection_name='feed', message=status)   #to post the status on user facebook
        print "Status is updated , Please check your facebook pofile..."


elif choice ==8:
        print "Scanning all IP and MAC address... "
	os.system('ifconfig')                               #to get the IP and MAC address


	

else :
	print "Enter the correct choice"                    #to warn user to enter a correct choice
