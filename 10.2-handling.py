# error handling => hata yönetimi

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except ZeroDivisionError:
#     print('y için 0 girilemez.')
# except ValueError:
#     print('x ve y için sayısal değer girmelisiniz.')

###############

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except (ZeroDivisionError,ValueError):
#     print('Yanlış bilgi girdiniz.')

###############

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as e:
#     print('Yanlış bilgi girdiniz.')
#     print(e)

###############

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except:
#     print('Yanlış bilgi girdiniz.')

###############
# Kullanıcı bilgileri doğru girene kadar program devam eder.
# Yanlış girdiğinde uyarıyı verir. ve tekrar bilgi ister.
# Bilgi doğru girildiğinde program sonlanır.
while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as ex:
        print('Yanlış bilgi girdiniz.', ex)  #ex e hangi hata kodu olduğunu ekrana gösterir.
    else:
        break
    finally:  # try veya except hangisi çalışırsa çalışsın bu blok çalışır.
        print('try except sonlandı.')
