import phonenumbers
print('ведити номер телефона с +')
r = input()
x = phonenumbers.parse(r)
print(x)