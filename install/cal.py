import color
t = "********** Калькулятор v 1.5 **********"
color.YELLOW_FEOLED(t)
print('Введите q для выхода')
while True:
	s = input("знак (+,-,*,/): ")
	if s == 'q': break
	if s in ('+', '-', '*', '/'):
		x = float(input("x= "))
		y = float(input("y= "))
		if s == "+":
			print("%5f" % (x+y))
		if s == "-":
			print("%5f" % (x-y))
		elif s == "*":
			print("%5f" % (x*y))
		elif s == "/":
			if y != 0:
				print("%5f" % (x/y))
			else:
				print("Вы ДоЛБоЁБ")
	else:
		print("Вы ДоЛБоЁБ")
