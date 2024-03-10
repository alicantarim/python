# def changeName(n):
#     n = 'ada'

# name = 'yiğit'

# changeName(name)
# print(name)


# def change(n):
#     n[0] = 'istanbul'

# sehirler = ['ankara', 'izmir']

# change(sehirler)
# print(sehirler)


# def change(n):
#     n[0] = 'istanbul'

# sehirler = ['ankara', 'izmir']

# change(sehirler[:])
# print(sehirler)


# def add(a, b, c = 0, d = 0, e = 0):
#     return sum((a,b,c))

# print(add(10, 20))
# print(add(10, 20, 30))


# def add(*params):
#     return sum((params))

# print(add(10, 20))
# print(add(10, 20, 30))
# print(add(10, 20, 30, 50, 60, 80))


def displayUser(**args):
    for key, value in args.items():
        print('{} is {}' .format(key,value))

displayUser(name = 'Çınar', age = 2, city = 'İstanbul')
displayUser(name = 'Ada', age = 12, city = 'Kocaeli', phone = '1213')
displayUser(name = 'Yiğit', age = 14, city = 'Ankara', phone = '121321', email = 'yigit@gmail.com')


def myFunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10, 20, 30, 40, 50, key1 = 'value 1', key2 = 'value')
