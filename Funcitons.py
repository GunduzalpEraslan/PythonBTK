'''
# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.

def yazdir(kelime ,adet):
    print(kelime * adet )


yazdir('merhaba\n', 5)

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.

def listYap(*params):
    liste=[]

    for param in params:
        liste.append(param)

    return  liste
result = listYap(10,20,30,'Merhaba')

print(result)
'''
'''
# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

def asalBul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2):
        if sayi > 1:
            for i in range(2,sayi):
                if(sayi%i == 0):
                    break
                else:
                    print(sayi)
sayi1 = int(input('Say1:'))
sayi2 = int(input('Say2:'))

asalBul(sayi1,sayi2)
'''



# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.
sayi = int(input('sayi : '))
def tamBolenler(sayi):
    liste = []
    for i in range(1,sayi+1):
        if sayi%i == 0:
            liste.append(i)
    print(liste)

tamBolenler(sayi)





