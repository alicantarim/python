# liste = [1,2,3,4]

# for i in liste:
#     print(i)

############## ----------------------------- #################

liste =[1,2,3,4,5]

# iterator = iter(liste)
# print(next(iterator))  #listedeki 1. eleman gelir.
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

############## ----------------------------- #################

# iterator = iter(liste)

# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break

############## ----------------------------- #################

class MyNumbers:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration
        
liste = MyNumbers(10,20)

# for x in liste:
#     print(x)   # 10,11,12,13,....,20 ekrana yazar.


myiter = iter(liste)
# print(next(myiter)) # 10
# print(next(myiter)) # 11
# print(next(myiter)) # 12
# print(next(myiter)) # 13
# print(next(myiter)) # 14


while True:
    try:
        element = next(myiter)
        print(element)
    except StopIteration:
        break
