'''numbers = [1,2,3,4,5]

for a in numbers:
    print('Hello')

names = ['çınar','sadık','sena']

for name in names:
    print(f'my name is {name}')

name = 'Sadık Turan'

for n in name:
    print(n)

tuple = [(1,2),(1,3),(3,5),(5,7)]

for a,b in tuple:
    print(a,b)

d = {'k1':1, 'k2':2, 'k3':3}

for key,value in d.items():
    print(key, value)
    '''
'''
sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayilar listesindeki hangi sayılar 3'ün katıdır ?

for a in sayilar:
    if a%3==0:
        print(a)

# 2- Sayilar listesinde sayıların toplamı kaçtır ?

toplam = 0
for a in sayilar:
    toplam += a
    print(toplam)

# 3- Sayilar listesindeki tek sayıların karesini alınız.

for a in sayilar:
    if a%2==1:
        print(a**2)
         '''
'''
sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

# 4- Şehirlerden hangileri en fazla 5 karakterlidir ?

for sehir in sehirler:
    if(len(sehir)>5):
        print(sehir.upper())
'''
urunler = [
    {'name': 'samsung S6', 'price': '3000'},
    {'name': 'samsung S7', 'price': '4000'},
    {'name': 'samsung S8', 'price': '5000'},
    {'name': 'samsung S9', 'price': '6000'},
    {'name': 'samsung S10', 'price': '7000'}
]
'''
# 5- Ürünlerin fiyatları toplamı nedir ?
toplam = 0
for urun in urunler:
    fiyat = int(urun['price'])
    toplam += fiyat
print(toplam)
'''
# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?
for urun in urunler:
    if(int(urun['price'])<=5000):
        print(urun['name'])


