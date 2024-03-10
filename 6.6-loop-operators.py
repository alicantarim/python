#####RANGE#####


# for item in range(10):    # 0 dan başlar 10 a kadar gider.
#     print(item)


# for item1 in range(2,20):    # 2 den başlar 20 a kadar gider.
#     print(item1)

# for item2 in range(50,100,10):    # 50 den başlar 100 a kadar 10 ar artarak gider.
#     print(item2)

# print(list(range(5,100,20)))



 ##### ENUMERATE #####

# index = 0
# greeting = 'Hello'

# for letter in greeting:
#     #print(f'index: {index} letter: {letter}')   Aşağıdaki ile aynı sonucu verir.
#     print(f'index: {index} letter: {greeting[index]}')
#     index += 1


greeting = 'Hello'

for index,letter in enumerate(greeting):
    print(f'index: {index} letter: {letter}') 


##### ZIP #####

list1 = [1,2,3,4,5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = [100, 200, 300, 400, 500]

print(list(zip(list1, list2, list3)))

for item in zip(list1, list2, list3):
    print(item)

for a,b,c in zip(list1, list2, list3):
    print(a,b,c)