import random

# result = dir(random)
# result = help(random)

result = random.random()  #0.0 - 1.0 arasında sayı üretir.
result = random.random() * 100
result = int(random.uniform(10,100)) #int yaparak decimal den kurtarırız.
result = random.randint(1,100)  #1 - 100 arasında tam sayı üretir.


greeting = 'hello there'
names = ['ali','yağmur','deniz','cenk']

result = names[random.randint(0,3)]
result = names[random.randint(0,len(names)-1)] #Aralık bilmediğimiz için len(names)-1

result = random.choice(names)  # listeyi verdiğinde rastgele seçip getirir.
result = random.choice(greeting)

liste = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] gelir.
random.shuffle(liste)    # [2, 6, 0, 1, 3, 5, 9, 4, 7, 8] elemanları karıştırarak gönderir.

result = liste

liste = range(100)
result =random.sample(liste, 3)  # [66, 28, 15]  0-100 arasında random 3 sayı getirir.
result =random.sample(names, 2)  # []'ali', 'deniz'] names listesi içinden random 2 kişiyi geitirir.
 

print(result)
