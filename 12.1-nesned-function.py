# def greeting(name):
#     print('hello',name)


# print(greeting('ali'))
# print(greeting)
    

# sayHello = greeting 

# Objeyi birbirine atama işlemi yaptığımzda atama işlemini
# bilginin tutulduğu yerdeki data değilde datanın adresini atıyoruz.

# print(sayHello)
# print(greeting)

# print(greeting('ali'))
# print(sayHello('ali'))

# del sayHello
# print(sayHello)
# print(greeting)



# encapsulation
# def outer(num1):
#     print('outer')
#     def inner_increment(num1):
#         print('inner')
#         return num1 + 1
#     num2 =inner_increment(num1)
#     print(num1, num2)

# outer(10)
# # inner_increment(10)  =>Tanımlanmaya bir değer verir. Sadece outer kapsamında çalıştırılacak olan bir değer.


def factorial(number):
    if not isinstance(number, int):
        raise TypeError('Number must be an integer')
    if not number >= 0:
        raise ValueError('Number must be zero or positive')

    def inner_factorial(number):
        if number <=1:
            return 1
        
        return number * inner_factorial(number -1)
    
    return inner_factorial(number)

try:
    print(factorial('4'))
except Exception as ex:
    print(ex)

