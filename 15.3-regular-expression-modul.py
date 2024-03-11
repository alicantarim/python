# Regular Expression Modülü
# Arama sonucunda sonuç döndürür.

import re

result = dir(re)

# re module

str = "Python Kursu: Python Programlama Rehberiniz | 40 saat  "

# re.findall()

# result = re.findall("Python",str)  # ['Python','Pyton']
# result = len(result)


# re.split()

# result = re.split(" ", str) 
# Her bir boşluk karakterinden ifadeyi böler ve liste şeklinde getirir.
# ['Python', 'Kursu:', 'Python', 'Programlama', 'Rehberiniz', '|', '40', 'saat', '', '']
# result = re.split("R", str)
# ['Python Kursu: Python Programlama ', 'ehberiniz | 40 saat  ']


# re.sub()

# result = re.sub(" ","-", str)
# Boşluk karakterlerini - ile değiştirir.


# re.search()

result = re.search("Python", str)
# Bulduğu ilk Python u match objesi olarak döndürür. 0-6 .ncı indexte olduğunu verir.
# result = result.span() # (0, 6)
# result = result.start() # Hangi karakterden başladığıı söyler 0
# result = result.end() #  Bitiş karakterinin söyler 6
# result = result.group() # Bulduğu ifadeyi gönderirir. Python
# result = result.string # Arama işlemindeki ifadeyi gönderir. Python Kursu: Python Programlama ', 'ehberiniz | 40 saat 


# regular expression




print(result)