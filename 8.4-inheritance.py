# Inheritance (Kalıtım): Miras alma

# Person => name, lastname, age, eat(), run(), drink()
# Student(Person), Teacher(Person)


# Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('Person Created')

    def whoAmI(self):
        print('I am a person')

    def eat(self):
        print('I am eating.')

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname) #Student class'ını oluşturduğumuzda Person ınıt metodunu da çalıştırmak için.
        self.studentNumber = number
        print('Student Created')

    # override
    def whoAmI(self):   #Bu method olmasaydı Student'ı çağırdığımızda Person daki method çalışacaktı.
        print('I am a student')

    def sayHello(self):
        print('Hello I am a student')

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch

    def whoAmI(self):
        print(f'I am a {self.branch} teacher.')

p1 = Person('Ali', 'Yılmaz')
s1 = Student('Çınar', 'Turan', 1254)
t1 = Teacher('Serkan', 'Yılmaz', 'Math')

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName)

p1.whoAmI()
s1.whoAmI() #Student whoAmI sahip değil ama Person dan geçiş yapabiliyor.
p1.eat()
s1.eat()
s1.sayHello()
t1.whoAmI()