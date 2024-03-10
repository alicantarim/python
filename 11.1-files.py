# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi,dosya_erisme_modu)
# dosya_erisme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w": (write) yazma modu. Dosya ya yazdığımızı ekler.
#   ** Dosyayı konumda oluşturur. 
#   ** Dosya içeriğini siler ve yeniden ekleme yapar. 


# file = open("newfile.txt", "w")
# file.close() # Dosyayı kapatır. Kaynakları tüketmemesi için


# file = open("newfile.txt", "w",encoding= 'utf-8')
# utf 8 -> Dosyanın içine yazılan Türkçe karakterleri vs tanıması için
# Burada Alican Tarım yazdığında 'ı' yı tanımıyor.


# file = open("newfile.txt", "w")
# file.write("Alican Tarım")
# file.close()

##########################################

# "a": (Append) ekleme. Dosya konumda yoksa oluşturur. Dosya ya ekleme yapar. Önceki bilgiler silinmez.

# file = open("newfile.txt", "a")
# file.write("Lavinya Tarım\n")
# file.close()

##########################################

# "x": (Create) oluşturma. Dosya zaten varsa hata verir.

# file = open("newfile2.txt", "x")

##########################################

# "r": (Read) okuma. Varsayılan. dosya konumda yoksa hata verir.

# try:
#     file = open("newfile2.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("Dosya okuma hatası")
# finally:
#     print("Dosya kapandı.")  
#     file.close() 


file = open("newfile.txt","r")

# for döngüsü

# for i in file:
#     print(i, end="")  #end="" print yazıldıktan sonra bir boşluk bırakmaması için

# *************** read() fonksiyonu

# content1 = file.read()

# print("İçerik 1")
# print(content1)

# # İçerik 1 yazıldıktan sonra dosyanın en sonuna gelir
# # Bu yüzden İçerik 2 de kaldığı yerden devam edeceğinden bir şey yazmaz.
# # Bu sebeple dosyaynı yeniden açma işlemini yapıyoruz.
# file = open("newfile.txt","r") 

# content2 = file.read()
# print("İçerik 2")
# print(content2)


# content = file.read(5) #İlk 5 karakteri alır.
# content = file.read(3) #5 karakter sonra ki 3 karakteri alır.
# content = file.read(3)
# print(content)

# *************** readline() fonksiyonu
# Her seferinde bir satırı okur.

# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")


# *************** readlines() fonksiyonu
# Her bir satır bilgiyi bir dizi elemanı olarak yazar.

liste = file.readlines()
print(liste)

file.close()