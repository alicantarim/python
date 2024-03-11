# def my_decorator(func):
#     def wrapper():
#         print("fonksiyondan önceki işlemler")
#         func()
#         print("Fonksiyondan sonraki işlemler")
#     return wrapper


# def sayHello():
#     print("hello")

# def sayGreeting():
#     print("greeting")

# sayHello = my_decorator(sayHello)
# sayHello()


# def my_decorator(func):
#     def wrapper():
#         print("fonksiyondan önceki işlemler")
#         func()
#         print("Fonksiyondan sonraki işlemler")
#     return wrapper


# @my_decorator  #decorator fonksiyonuna sayHello yu göndermiş oluyor.
# def sayHello():
#     print("hello")

# sayHello()

############## ----------------------------- #################


# def my_decorator(func):
#     def wrapper(name):
#         print("fonksiyondan önceki işlemler")
#         func(name)
#         print("Fonksiyondan sonraki işlemler")
#     return wrapper


# @my_decorator  #decorator fonksiyonuna sayHello yu göndermiş oluyor.
# def sayHello():
#     print("hello", name)

# sayHello("ali")


############## ----------------------------- #################

import math
import time

def calculateTime(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print(f"Fonksiyon {func.__name__} {finish-start} saniye sürdü.")
    return inner

@calculateTime
def usalma(a,b):
    print(math.pow(a,b))

@calculateTime
def faktoriyel(num):
    print(math.factorial(num))

@calculateTime
def toplama(a,b):
    print(a+b)

usalma(2,3)
faktoriyel(4)
toplama(4,2)