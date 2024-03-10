website = 'http://www.sadikturan.com'
course = 'Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)'

# 1- ' Hello World ' karkater dizisinin baş ve son boşluk karakterlerini silin.

result = ' Hello World '.strip()
result = ' Hello World '.lstrip()
result = ' Hello World '.rstrip()
result = website.lstrip('/:pth')


# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.

result = 'www.sadikturan.com'.strip('w.moc')

# 3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.

result = course.lower()
result = course.upper()
result = course.title()  #Her kelimenin baş harfi büyür.

# 4- 'websitesi' içinde kaç tane a karakter vardır. (count('a'))

result = website.count('a')
result = website.count('www')
result = website.count('www',0,10)  # 0-10 index arasında kaç tane var.

# 5- 'website' www" ile başlayıp com ile bitiyor mu ?

result = website.startswith('www')
result = website.startswith('http')
result = website.endswith('com')

# 6- 'website' içinde '.com' ifadesi var mı?

result = website.count('.com')
result = website.find('com')   #com ifadesinin c nin index numarasını getirir.
result = course.find('Python')
result = course.rfind('Python')

result = website.index('com')
result = website.rindex('com')

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)

result =course.isalpha()
result = 'Hello'.isalpha()
result = course.isdigit()
result = '123'.isdigit()

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

result = 'Contents'.center(50,'*')
result = 'Contents'.ljust(50,'*')
result = 'Contents'.rjust(50,'*')

# 9- 'course' karkater dizisindeki tüm boşluk karakterlerini '-' ile değiştir.

result = course.replace(' ','-') 
result = course.replace(' ','-',5)  #Sadece ilk 5 boşluğu - ile değiştirir.
result = course.replace(' ','',)

# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin.

result = 'Hello World'.replace('World','There')

# 11- 'course' karakter dizisini boşluk karakterlerinden ayırın.

result = course.split(' ')
result = result[2]

print(result)