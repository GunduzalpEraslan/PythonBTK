
sehirler = ['Kocaeli','istanbul']
plakalar = [41, 34]
"""
print(plakalar[sehirler.index('istanbul')])
print(plakalar[sehirler.index('Kocaeli')])
"""
# print(plakalar['kocaeli']) => 41
# print(plakalar['istanbul']) => 34

plakalar = { 'kocaeli' : 41, 'istanbul': 34 }

print(plakalar['kocaeli'])
# print(plakalar['istanbul'])

# plakalar['ankara'] = 6
# plakalar['kocaeli'] = 'new value'

# print(plakalar)

users = {
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

print(users['cinarturan'])
