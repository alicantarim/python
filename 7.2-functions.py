# def sayHello():
#     print('Hello')

# sayHello()


# def sayHello(name = 'user'):
#     print('Hello '+ name)

# sayHello('Çınar')
# sayHello('Ada')
# sayHello()


# def sayHello(name = 'user'):
#     return ('Hello '+ name)

# msg = sayHello('Çınar')
# print(msg) 


# def total(num1, num2):
#     return num1 + num2

# result = total(10,20)
# print(result)


def yasHesapla(dogumYili):
    return 2019 - dogumYili

ageCinar = yasHesapla(2017)
ageAda = yasHesapla(2010)

print(ageCinar, ageAda)



def emeklilikKacYilKaldi(dogumYili, isim):
    '''
    DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldi
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil bilgisi
    '''

    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if (emeklilik > 0):
        print(f'{isim} emekliliğinize {emeklilik} yıl kaldı.')
    else:
        print('Zaten emekli oldunuz.')

emeklilikKacYilKaldi(1983, 'Ali')
emeklilikKacYilKaldi(1999, 'Mehmet')

print(help(emeklilikKacYilKaldi))

list = [1,2,3]

print(list.append())

