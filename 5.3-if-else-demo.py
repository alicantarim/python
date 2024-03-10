# # 1- Kullanıcıdan isim yaş ve eğitim bilgilerini isteyip ehliyet alabilme
#     durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu
#     lise ya da üni olmalıdır.


# isim = input('İsminiz: ')
# yas = int(input('Yaşınız: '))
# egitim = input('Eğitim: ')

# if (yas >= 18):
#     if (egitim == 'lise' or egitim == 'üniversite'):
#         print(f'{isim} Ehliyet alabilirsiniz.')
#     else:
#         print(f'{isim} Ehliyet alamazsınız eğitim durumunuz yetersiz.')
# else:
#     print(f'{isim} Ehliyet alamazsınız yaşınız tutmuyor.')





# # 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#     not aralığına karşılık gelen not bilgisini yazdırınınz.
#     0-24 => 0
#     25-44 => 1
#     45-54 => 2
#     55-69 => 3
#     70-84 => 4
#     85-100 => 5


# yazili1 = float(input('1.yazili: '))
# yazili2 = float(input('2.yazili: '))
# sozlu = float(input('Sözlü: '))

# ortalama = (yazili1 + yazili2 + sozlu) / 3

# if (ortalama >= 0) and (ortalama < 25):
#     print(f'Ortalamanız: {ortalama} notunuz: 0')
# elif (ortalama >= 25) and (ortalama < 45):
#     print(f'Ortalamanız: {ortalama} notunuz: 1')
# elif (ortalama >= 45) and (ortalama < 55):
#     print(f'Ortalamanız: {ortalama} notunuz: 2')
# elif (ortalama >= 55) and (ortalama < 70):
#     print(f'Ortalamanız: {ortalama} notunuz: 3')
# elif (ortalama >= 70) and (ortalama < 85):
#     print(f'Ortalamanız: {ortalama} notunuz: 4')
# elif (ortalama >= 85) and (ortalama <= 100):
#     print(f'Ortalamanız: {ortalama} notunuz: 5')
# else:
#     print('Yanlış bilgi girdiniz.')




# # 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
#     göre hesaplayınız.
#     1. Bakım => 1. yıl
#     2. Bakım => 2. yıl
#     3. Bakım => 3. yıl
#     ** Süre hesabını alınan gün ay yıl bilgisine göre gün bazlı hesaplaynızı.
#     *** datetime modülünü kullanmamız gerekiyor.
#     (simdi) - (2018/8/1) => gün



# days = int(input('Aracınız kaç gündür trafikte: '))

# if days <= 365:
#     print('1.servis aralığı')
# elif days > 365 and days <= 365*2:
#     print('2.servis aralığı')
# elif days > 365*2 and days <= 365*3:
#     print('3.servis aralığı')
# else:
#     print('Hatalı süre bilgisi')


import datetime

tarih = input('Aracınız hangi tarihte trafiğe çıktı (2019/8/9): ')
tarih = tarih.split('/')
# print(tarih[0])
# print(tarih[1])
# print(tarih[2])

trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
#print(simdi)
fark = simdi - trafigeCikis
#print(fark)
days = fark.days
#print(days)
 

if days <= 365:
    print('1.servis aralığı')
elif days > 365 and days <= 365*2:
    print('2.servis aralığı')
elif days > 365*2 and days <= 365*3:
    print('3.servis aralığı')
else:
    print('Hatalı süre bilgisi')