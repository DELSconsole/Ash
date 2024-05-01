clear = lambda: os.system('cls')
from sys import argv
import time
import os
import socket
import shutil
import requests
jls_extract_var = """
[1]-установить комманду
[2]-все комамнды
"""
print(jls_extract_var)
jls_extract_var = input
select = jls_extract_var(":")
if select == '1':
	def save_from_www(link):
		filename = link.split('/')[-1]
		r = requests.get(link, allow_redirects=true)
		open(filename, "w").write(r.content)
	i = input()
	link1 = i
	save_from_www(link1)

