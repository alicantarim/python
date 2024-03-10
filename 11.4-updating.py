# DOSYADA GÜNCELLEME YAPMA
# r+   => Hem okuma hem yazma modu


# with open("newfile.txt","r+", encoding="utf-8") as file:
#     file.seek(20)
#     file.write("deneme")

# with open("newfile.txt","r+", encoding="utf-8") as file:
#     print(file.read())


# ******** SAYFA SONUNDA GÜNCELLEME ********

# with open("newfile.txt","a",encoding="utf-8") as file:
#     file.write("\nDeneme Deneme")


# ******** SAYFA BAŞINDA GÜNCELLEME ********

# with open("newfile.txt","r+", encoding="utf-8") as file:
#     content = file.read()
#     content = "Efe Turan\n" +content 
#     file.seek(0)
#     file.write(content)

# with open("newfile.txt","r", encoding="utf-8") as file:
#     print(file.read())


# ******** SAYFA ORTASINDA GÜNCELLEME ********
    
# with open("newfile.txt","r+", encoding="utf-8") as file:
#     list = file.readlines()   # İçerik bir dizi şeklinde gelir.
#     list.insert(1,"Ali Korkmaz\n") #1. indexe Ali Korkmaz'ı ekler.
#     file.seek(0) #sayfanın en başına gideriz.
#     for i in list:  #for döngüsüyle tüm listeyi sayfaya yazıyoruz.
#         file.write(i)

# with open("newfile.txt","r", encoding="utf-8") as file:
#     print(file.read())



with open("newfile.txt","r+", encoding="utf-8") as file:
    list = file.readlines()   # İçerik bir dizi şeklinde gelir.
    list.insert(1,"Atila Yılmaz\n") #1. indexe Ali Korkmaz'ı ekler.
    file.seek(0) #sayfanın en başına gideriz.
    file.writelines(list) #FOR döngüsü kullanmak yerine 'writelines' metodunu kullanabiliriz.

with open("newfile.txt","r", encoding="utf-8") as file:
    print(file.read())
    