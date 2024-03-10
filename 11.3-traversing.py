# DOSYA OKUMA FONKSİYONLARI

# file = open("newfile.txt","r",encoding="utf-8")

# content = file.read()
# print(content)

# file.close()

## with ile Kod bloğunun sonuna geldiği zaman dosya direk kapanır.
## file.close() kullanama gerek kalmaz.
with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read(10) #ilk baştan 10 tanesini okur.
    print(content)
    file.seek(0) # krüsörü 0 konumuna (en başa) gönderir. veya kaç yazarsak oraya gönderir.
    print(file.tell()) #krüsörün konumu verir. Örn. 45 gibi
    content2 = file.read()
    print(content2)