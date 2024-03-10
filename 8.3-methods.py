# class

'''

class Person:
    # class attributes
    address = 'no information'

    # constructor (yapıcı metod)
    def __init__(self,name, year):
       
        # object attributes
        self.name = name
        self.year = year

    # instance methods
    def intro(self):
        print('Hello There. I am ' + self.name)

    # instance methods
    def calculateAge(self):
        return 2019 - self.year

# object, (instance)
p1 = Person(name = 'Ali', year = 1990)
p2 = Person('Kübra', 1995)

p1.intro()
p2.intro()

print(f'adım: {p1.name} Yaşım: {p1.calculateAge()}')
print(f'adım: {p2.name} Yaşım: {p2.calculateAge()}')

'''


#########################

class Circle:
    # Class object attribute
    pi = 3.14

    def __init__(self, yaricap = 1):
        self.yaricap = yaricap

    #Methods
    def cevreHesapla(self):
        return 2 * self.pi * self.yaricap
    
    def alanHesapla(self):
        return self.pi * (self.yaricap ** 2)
    
c1 = Circle()  # yaricap = 1 olarak kabul eder.
c2 = Circle(5)

print(f'c1 : alan = {c1.alanHesapla()} çevre = {c1.cevreHesapla()}')
print(f'c2 : alan = {c2.alanHesapla()} çevre = {c2.cevreHesapla()}')
