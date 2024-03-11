# İşletim sistemi üzerindeki bilgileri sunar.
# Klasörler hakkında bilgiye sahip olabilirsiniz.
# Dosyalarla alakalı işlemleri yapabilirsiniz.

import os
import datetime
# result = dir(os)
# result = os.name # İşletim sistemini söyler 'posix'
# result = os.getcwd() #15.2-os-modul.py dosyasının hangi klasör içerisinde olduğunu söyler.
# os.mkdir("newdirectory") # Dizin içerisine newdirectory adında klasör oluşturur.

# Klasör Oluşturma
# os.makedirs("newdirectory/yeniklasör")
# os.rename("newdirectory","yeniklasör")  # Klasör ismini değiştirme
# os.rmdir("newdirectory") # Klasörü siler.
# os.removedirs("yeniklasör/yeniklasör") #Alt dizinleri siler.

#dizin değiştirme
# os.chdir('C:\\')

# listeleme
# result = os.listdir()
# result = os.listdir('C:\\') #C dizini altındaki bütün klasör ve dosyaları listeler

# Sadece py uzantılı dosyaları görürürz. Filtreleme
# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)

# Etkin dizin altında dosya hakkında bilgi sahibi olmak için
# result = os.stat("15.2-os-modul.py")
# result = result.st_size / 1024  # dosya boyutu byte cinsinde olduğu için 1024 bölüm kB olarak çevirdik
# result = datetime.datetime.fromtimestamp(result.st_ctime)  # Oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime)  # Son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime)  # Değiştirilme tarihi

# os.system("notepad.exe")   #İstediğimiz bir programı çalıştırabiliriz.


# Path 
# Dosya uzantıları üzerinde işlemler yapılır.

result = os.path.abspath("15.2-os-modul.py") # Dosyanın tam konumunu (yolunu) belirtir.
result = os.path.dirname("/Users/alicantarim/Desktop/python_temelleri/Deneme/15.2-os-modul.py") #Tam konumu verilen dosyanın dizin ismini alıyoruz.
result = os.path.dirname(os.path.abspath("15.2-os-modul.py"))
result = os.path.exists("15.2-os-modul.py") # İlgili konumda bu dosya var mı yok mu bunu verir. (True,False)
result = os.path.isdir("15.2-os-modul.py") # Verdiğimiz yol klasör mü diye bakar. (True,False) klasör olmadığı için False verir.
result = os.path.isfile("15.2-os-modul.py") # Verdiğimiz yol dosya mı diye bakar. True döner
result = os.path.join("C:\\","deneme","deneme1")
result = os.path.split("C:\\deneme")
result = os.path.splitext("15.2-os-modul.py") # Ulaştığımız dosyanın ismi ve uzantasını ayırır.
# result = result[0]
result = result[1]

print(result)