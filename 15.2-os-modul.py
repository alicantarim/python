# İşletim sistemi üzerindeki bilgileri sunar.
# Klasörler hakkında bilgiye sahip olabilirsiniz.
# Dosyalarla alakalı işlemleri yapabilirsiniz.

import os
result = dir(os)
result = os.name # İşletim sistemini söyler 'posix'
result = os.getcwd() #15.2-os-modul.py dosyasının hangi klasör içerisinde olduğunu söyler.
os.mkdir("newdirectory") # Dizin içerisine newdirectory adında klasör oluşturur.



print(result)