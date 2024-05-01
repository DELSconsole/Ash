import time
import os
import color
clear = lambda: os.system('cls')
clear()
jls_extract_var = "                                                                           "
t = jls_extract_var + time.strftime("%H:%M:%S") + jls_extract_var + time.strftime("%d/%m/%Y")
color.YELLOW_FEOLED(t)