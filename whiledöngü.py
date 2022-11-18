'''
sayilar = [1,3,5,7,9,12,19,21]

# 1: sayilar listesini while ile ekrana yazdırın.

i=0
while(i<len(sayilar)):
    print(sayilar[i])
    i+= 1

# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.

baslangıc = int(input("Başlangıç değerini girniiz : "))
bitis = int(input("Bitiş değerini giriniz : "))

i = baslangıc
while i<bitis:
    i+=1
    if(i%2 ==1):
        print(i)
'''
'''
# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
i=100
while i>0:
    i-=1
    print(i)
'''
'''
# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde
#    yazdırın.
numbers =[]
i=0
while i<5:
    sayi = int(input(f' {i+1}. sayıyı giriniz: '))
    numbers.append(sayi)
    i+=1
numbers.sort()
print(numbers)
'''

# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (name, price) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

urunler = []
adet = int(input('Kaç tane ürün adedi gireceksiniz? -->'))
i =0
while i<adet:
    name = input('Ürün ismi :')
    price = input('Ürün fiyatı :')
    urunler.append({'name':name,
                    'price':price})
    i+=1

    for urun in urunler:
        print(f'Ürün adı : {urun["name"]} \t Ürün fiyatı : {urun["price"]}')
