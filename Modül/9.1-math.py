# YÖNTEM 1
# import math
import math as islem
# value = dir(math)
# value = help(math)
# value = help(math.factorial)

# value = math.sqrt(49)    #karekök
# value = math.factorial(5)
# value = math.floor(5.9)  #aşağı yuvarlar 5
# value = math.ceil(5.9)   #yukarı yuvarlar 5

# value = islem.factorial(5)


# YÖNTEM 2
# from math import *  
# İlgili modülden neleri almak istersek kullanırız. * hepsini alır. 
# Tüm fonks. import ettiğimizden Modül ismini kulanmadan yapabiliriz.

def sqrt(x):
    print('x :'+ str(x))



from math import factorial,sqrt,ceil
# Sadece factorial, sqrt ve ceil kullanabiliriz.

# value = factorial(5)
value = sqrt(9)
# value = ceil(9.8)

print(value)