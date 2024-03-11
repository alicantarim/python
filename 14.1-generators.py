# Bellekte yer işgal etmeyen iterator üretir.

# def cube():
#     result = []

#     for i in range(5):
#         result.append(i**3)
#     return result

# print(cube())


# yield bir değer üretir gönderir ve sonra saklamaz.
# 2. defa ulaşmak istersek ulaşamayız.
# Üretildiği anda kullanılmak için
# def cube():
#     for i in range(5):
#         yield i ** 3
# # Generator üzerinden bir bilgi istersek o anda yield çalıştırılır.
# # Dondurulur ve tekrar istersek tekrar çalıştırılır.

# for i in cube():
#     print(i)


liste = [i**3 for i in range(5)]

print(liste) # [0,1,8,27,64]


generator = (i**3 for i in range(5))

print(generator)

# print(next(generator))
# print(next(generator))
# print(next(generator))

for i in generator:
    print(i)  # 0 1 8 27 64