# 1-100 e kadar sayıları ekranda gösterelim.


# x = 0

# while x <= 100:
#     if ( x % 2 == 1):
#         print(f'sayı tek: {x}')
#     else:
#         print(f'sayı çift: {x}')
#     x += 1

# print('Bitti')

name = '' #False

while not name.strip():  # Kullanıcı boşluk girerse strip komutuyla bunu siliyoruz.
    name = input('isminizi giriniz: ') 

print(f'Merhaba, {name}')

