#key - value

#41 => kocaeli  34 => istanbul

# sehirler = ['Kocaeli', 'İstanbul']
# plakalar = [41, 34]

# print(plakalar[sehirler.index('Kocaeli')])

#print(plakalar['Kocaeli']) => 41

#plakalar = { 'key' : 'value' }
# plakalar = { 'Kocaeli' : 41, 'İstanbul' : 34 }

# print(plakalar['Kocaeli'])
# print(plakalar['İstanbul'])

# plakalar['Ankara'] = 6
# plakalar['Kocaeli'] = 'new value'

# print(plakalar)


users = {
    'sadikturan': 36,
    'cinarturan': 2
}

print(users['cinarturan'])

users2 = {
    'sadikturan': {
        'age': 36,
        'roles': ['user'],
        'email': 'sadik@gmail.com',
        'address': 'kocaeli',
        'phone': '1231321'
    },
    'cinarturan': {
        'age': 2,
        'roles': ['admin','user'],
        'email': 'cinar@gmail.com',
        'address': 'kocaeli',
        'phone': '1231321'
    }
}

print(users2['cinarturan'])
print(users2['cinarturan']['age'])
print(users2['cinarturan']['email'])
print(users2['cinarturan']['address'])
print(users2['cinarturan']['roles'][0])