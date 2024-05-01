import time
import os
import color
clear = lambda: os.system('cls')
print('ведите время')
n = int(input())
for i in range(n):
	clear()
	jls_extract_var = "                                                                           "
	t = jls_extract_var + time.strftime("%H:%M:%S") + jls_extract_var + time.strftime("%d/%m/%Y")
	color.WIE_FEOLED(t)
	time.sleep(1)