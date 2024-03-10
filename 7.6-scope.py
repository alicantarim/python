# global scope
# x = 'global x'

# def function():
    # local scope
#     x = 'local x'
#     print(x)

# function()
# print(x)


############################

# name = 'Çınar'

# def changeName(new_name):
#     name = new_name
#     print(name)

# changeName('Ada')
# print(name)

#EKRANA ÖNCE 'ADA' SONRA 'ÇINAR' YAZAR.

############################

name = 'global string'

def greeting():
    name = 'Lavinya'

    def hello():
        name = 'Kübra'
        print('hello ' + name)

    hello()

greeting()

############################

x = 50

def test(x):
    print(f'x: {x}')

    x = 100
    print(f'changed x to {x}')

test(x)
print(x)

    # 50 - 100 - 50

############################

x = 50

def test():
    global x  # global tanımladığımızda tüm değişiklikler yukarıdaki x üzerinde yapılır.
    print(f'x: {x}')
    x = 100
    print(f'changed x to {x}')

test()
print(x)

    # ÇIKTI: 50 - 100 - 100


