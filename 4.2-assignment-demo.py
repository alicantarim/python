x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6
 
# 1- Kullanıcıdan aldığınız 2 sayının çarpımın ile x,y,z, toplamının farkı nedir

# a  = int(input('1. sayı: '))
# b  = int(input('2. sayı: '))

# result = (a *b) - (x+y+z)
# print(result)

# 2- y nin x e kalansız bölümünü hesaplayınız.

result = y // x 

# 3- x,y,z toplamının mod 3 ü nedir.

toplam = (x+y+z)
result = toplam % 3

# 4- y nin x kuvvetini hesaplayınız

result = y ** x

# 5- x, *y, z = numbers işlemine göre z nin küpü kaçtır
numbers = 1, 5, 7, 10, 6
x, *y, z = numbers
result = z ** 3
print(z)

# 6- x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır.
x, *y, z = numbers

result = y[0] + y[1] + y[2]

print(result)