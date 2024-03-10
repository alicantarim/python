# def square(num):
#     return num ** 2

# result = square(2)
# print(result)
 
##########################

# def square(num):
#     return num ** 2

# numbers = [1,3,5,9]
# result = list(map(square, numbers))  #işlemi liste şeklinde ekrana yazar.

# print(result)

# for item in map(square, numbers):    #işlemi alt alta ekrana yazar.
#     print(item)


##########################


# numbers = [1,3,5,9]
# result = list(map(lambda num: num ** 2, numbers))

# print(result)
    

##########################

# square = lambda num: num ** 2

# result = square(3)

# print(result)


##########################
# FILTER ICERIDEN GELEN SAYILARIN ORN: SADECE TEKLER VEYA ÇIFTLER GERİ DÖNSÜN

# MOD ALIP 2  ye BOLUMDEN KALAN 0 OLANLARI TRUE
# KALAN 1 ISE FALSE GÖNDER 
numbers = [1,3,5,9,10,4]

# def check_even(num):
#     return num % 2 == 0

# result = list(filter(check_even, numbers))

# print(result)

##########################

# result = list(filter(lambda num: num % 2 == 0, numbers))

# print(result) 

##########################

check_even = lambda num: num % 2 == 0

result = list(filter(check_even, numbers))
#result = check_even(numbers[2])  # 2.indexteki sayı için True False döndürür.

print(result)