# CSC 842 Cycle 9 Ping Communicator Program by Max Gorbachevsky
# This program creates ping packet with added encrypted payload. The receiver can receive the ping packets and decrypt the payload.

import sys
from scapy.all import *
from connection import ip
import base64

# send encrypted message module
def sendMessage():
    print("pinging the target....")
    message = str(input("\nEnter your message here:  >> "))
    encodedMessage = base64.b64encode(message.encode("utf-8"))
    encodedStr = str(encodedMessage, "utf-8")
    icmp = (IP(dst=ip)/ICMP(type=8)/ (encodedMessage))
    resp = sr1(icmp,timeout=10)
    if resp == None:
        print("This host is down")
    else:
        print("Message sent")

# Receive message module
def receiveMessage():
    pkts=sniff(filter="icmp", timeout=120,count=15)

    for packet in pkts:
        if packet.haslayer(ICMP) and str(packet.getlayer(ICMP).type)=="8":
            encodedMessage = (repr(packet[IP].payload)[74:-4])
            decodedMessage = base64.b64decode(encodedMessage).decode('utf-8', errors='ignore')
            print(decodedMessage)
        
# Choice function for Main Menu
def getChoice():
    while True:
        try:
            choice = input("Enter selection  >> ")
            if choice in ["q","Q","quit","Quit","exit"]:
                quit()
            elif choice in ["b"]:
                return choice
            try:
                int(choice)    
            except ValueError:
                print("ERROR: must enter integer")
                continue
        except KeyboardInterrupt:
            quit()
        return choice


# Main Menu
def mainMenu():
    print("Welcome to Communicator")
    print("\n\t##############\n\t   Main Menu\n\t##############")
    print("\nPlease select from the following options")
    print("\t1 - Send a message")
    print("\t2 - Receive a message")
    print("\tq - quit")
    print("\n")
    choice = getChoice()
    if choice == "1":
        print("Sending the message (control + c to stop)")
        sendMessage()
    if choice == "2":
        print("Receiving the message (control + c to stop)")
        receiveMessage()
    
# Start
while True:
    mainMenu()