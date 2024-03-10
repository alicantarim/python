numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

val = min(numbers)
val = max(numbers)
val = min(letters)
val = max(letters)

val = numbers[3:6]
val = numbers[:3]
val = numbers[4:]

numbers[4] = 40
numbers.append(49)  #sonuna 22 rakamını ekler.
numbers.append(59)
numbers.insert(3, 78) #3. indexe 78 rakamını ekler.
numbers.insert(-1, 52) #listenin en sonundan bir öncekine 52 yi ekler.

#numbers.pop()  #Sondaki rakamı siler.
#numbers.pop(0) #0. indexi siler.
#numbers.remove(49) #Silmek istediğin karakteri veriyoruz. 49 rakamını siler.

numbers.sort()  #sort kucukten buyuge sıralar.
letters.sort()
numbers.reverse() #reverse buyukten kucuge sıralar.
letters.reverse()

print(numbers)
print(letters)

print(len(numbers))
print(len(letters))

print(numbers.count(10)) #numbers içinde 10 dan kaç tane var gösterir.
print(letters.count('a'))

numbers.clear() #Tum elemanları siler.