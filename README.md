# CSC842-Summer-2023-Cycle9

**Ping Communicator**

I almost ran out of ideas for an original project this cycle. I didn’t want to break the rule and build upon any previous projects. During the review of Cycle 8 projects and seeing the stego project GIFEncode by Allen Willan, I thought of another way to convey hidden messages. ICMP Ping packets have an optional payload space.

I used Scapy to build and send Ping packets to a known destination. In the optional Payload space, I added an encrypted message. The program also has a receiver option to receive the packets and decode the message.

**Three main ideas:**
1.	ICMP packets have optional Payload Data space. This space could be used for sending hidden messages.
2.	Scapy allows to create/read network packets and to send/receive ones.
3.	Base64 is a simple encryption scheme that could be used for easy encryption implementation.

**Limitations and future work**
The main limitation of the project is time. In the future, I would like to add an option of taking long text, encrypting it, and splitting the encrypted message to fit multiple ping packets that would be later stripped by the receiver, combined together, and decrypted. The same could be done with files.

**Running the program**
To configure and run the program, the ping.py and connection.py files need to be saved at both communication endpoints. The user needs to add the other end IP address to the communication.py file.
