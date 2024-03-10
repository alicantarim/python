sayilar = [1,3,5,7,9,12,19,21]

#  1- Sayılar listesini while ile ekrana yazdırın.

# i = 0

# while (i < len(sayilar)):
#     print(sayilar[i])
#     i += 1
    
#  2- Başlangıç ve bitiş değerlerinin kullanıcıdan alıp aradaki tüm
#     tek sayıları ekrana yazdırın.

# baslangic = int(input('Başlangıç: '))
# bitis = int(input('Bitiş: '))

# i = baslangic
# while i < bitis:
#     i += 1
#     if (i % 2 == 1):
#         print(i)


#  3- 1-100 arasındaki sayıları azalan şekilde yazdırın.

# x = 100
# while x > 0:
#     print(x)
#     x -= 1



#  4- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde
#     yazdırın.

# numbers = []

# i = 1

# while i <6:
#     sayi = int(input(f'{i}.Sayıyı giriniz: '))
#     numbers.append(sayi)
#     i += 1

# numbers.sort()  #Kullanıcıdan aldığımız sayıları sıralıyoruz.

# print(numbers)



# 5- Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#     ** ürün sayısını kullanıcıya sorun.
#     ** dictionary listesi yapısı (name, price) şeklinde olsun.
#     ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

urunler = []

adet = int(input('Kaç ürün eklemek istiyorsunuz: '))
i = 0

while (i<adet):
    name = input('Ürün ismi: ')
    price = int(input('Ürün Fiyatı: '))
    urunler.append({
        'name': name,
        'price': price
    })
    i += 1

for urun in urunler:
    print(f'Ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}')
