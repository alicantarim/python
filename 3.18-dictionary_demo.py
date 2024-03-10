'''
ogrenciler = {
    '120': {
        'ad': 'Ali',
        'soyad': 'Yılmaz',
        'telefon': '532 000 00 01'
    },
    '125': {
        'ad': 'Can',
        'soyad': 'Korkmaz',
        'telefon': '532 000 00 02'
    },
    '128': {
        'ad': 'Volkan',
        'soyad': 'Yükselen',
        'telefon': '532 000 00 03'
    }
}

1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız 
   bilgilerle dictionary içinde saklayınız.

2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
'''

ogrenciler = {}

number = input("Öğrenci No: ")
name = input("Öğrenci Adı: ")
surname = input("Öğrenci Soyad: ")
phone = input("Öğrenci Telefon: ")

# ogrenciler[number] = {
#     'ad': name,
#     'soyad': surname,
#     'telefon': phone
# }

# print(ogrenciler)

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})

number = input("Öğrenci No: ")
name = input("Öğrenci Adı: ")
surname = input("Öğrenci Soyad: ")
phone = input("Öğrenci Telefon: ")

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})

number = input("Öğrenci No: ")
name = input("Öğrenci Adı: ")
surname = input("Öğrenci Soyad: ")
phone = input("Öğrenci Telefon: ")

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})

#print(ogrenciler)
print('*'*50)

ogrNo = input('Öğrenci No: ')
ogrenci = ogrenciler[ogrNo]

#print(ogrenci)
print(f'Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}')       