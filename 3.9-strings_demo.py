website = 'http://www.sadikturan.com'
course = 'Python Kursu: Baştan sona python programlama rehberiniz (40 saat)'

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır.

result = len(course)
length = len(website)


# 2- 'website' içinden www karakterlerini alın.

result = website[7:10]


# 3- 'website' içinden com karakterlerini alın.

result = website[22:25]
result = website[length-3:length]

# 4- 'course içinden ilk 15 ve son 15 karakterlerini alın.

result = course[0:15]
result = course[:15]
result = course[-15:]


# 5- 'Course' ifadesindeki karakterleri tersten yazdırın

result = course[::-1]

s = '12345' * 5
print(s[::5])


name, surname, age, job = 'Bora', 'Yılmaz', 32, 'Muhendis'

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
# Benim adım bora yılmaz, yaşım 32 ve mesleğim mühendis.

result = 'Benim adım '+ name + ' ' + surname + ', Yaşım ' + str(age) + ' ve mesleğim ' + job
result = 'Benim adım {} {}, Yaşım {} ve mesleğim {}.' .format(name,surname,age,job)
result = 'Benim adım {0} {1}, Yaşım {2} ve mesleğim {3}.' .format(name,surname,age,job)
result = f'Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}.'

# 7- 'Hello world' ifadesindeki w harfini W olarak değiştirin.
s = 'Hello world'
s = s[0:6] + 'W'+ s[-4:]
s.replace('w','W')

print(s)

# 8 - 'abc' ifadesini yan yana 3 defa yazdırın.

result = 'abc ' * 3





print(result)