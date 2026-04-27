#!/usr/bin/env python3

import time, os

def EnterInterface():
	print("Please run this script as root (sudo).")
	print("Enter network interface:")
	NetI = input("")
	Monitoring(NetI)

def Monitoring(NetI):
	os.system("airmon-ng start " + NetI)
	input("Press enter to stop monitoring")
	os.system("airmon-ng stop " + NetI + " mon")
	os.system("systemctl restart NetworkManager")
	print("[1] Start again")
	print("[2] Enter new network interface")
	MONOPT = input("")
	if MONOPT == "1":
		Monitoring(NetI)
	elif MONOPT == "2":
		EnterInterface()
		
EnterInterface()