# class

class Person:
    # class attributes
    address = 'no information'

    # constructor (yapıcı metod)
    def __init__(self,name, year):
        # object attributes
        self.name = name
        self.year = year
        print('init methodu çalıştı')


    # methods

# object, (instance)
p1 = Person(name = 'Ali', year = 1990)
p2 = Person('Kübra', 1995)

# updating
p1.name = 'Ahmet'
p1.address = 'Kocaeli'

# accessing object attributes
print(f'p1: name: {p1.name} year: {p1.year} address: {p1.address}')
print(f'p2: name: {p2.name} year: {p2 .year} address: {p2.address}')

print(p1)
print(p2)
print(type(p1))
print(type(p2))