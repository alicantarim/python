'''
x = input('1.sayı: ')
y = input('2.sayı: ')

print(type(x))
print(type(y))

toplam = int(x) + int(y)
print(toplam)
'''

'''
x = 5               #int
y = 2.5             #float
name = 'Cınar'      #string
isOnline = True     #bool

print(type(x))
print(type(y))
print(type(name))
print(type(isOnline))

x = float(x)
print(x)
print(type(x))
'''


'''
Daire Alanı     : πr²
Daire Çevresi   : 2πr

*Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. r:3.14
'''
pi = 3.14
r = float(input("yarı çap:" ))
alan = pi * (r ** 2)
cevre = 2 * pi * r 

print('alan', alan)
print('çevre', cevre)
print("alan: "+ str(alan) + " çevre: "+ str(cevre))
