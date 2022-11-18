'''
# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

a = int(input("Bir sayı giriniz : "))
if a<=100 and a>0:
    print("Aralık doğrudurç")
else:
    print("Aralık yanlıştır")
'''
'''
# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
a = int(input("Bir sayı giriniz : "))

if a>0 and a%2==0:
    print("Bu pozitif bir çift sayıdır")
else:
    print("Bu pozitif bir çift sayı değildir.")
    '''
# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
a = int(input("Bir sayı giriniz : "))
b = int(input("Bir sayı giriniz : "))
c = int(input("Bir sayı giriniz : "))

if (a > b) and  (a > c):
    print(f'a en büyük sayıdır')
elif  (b > a) and (b > c):
    print(f'b en büyük sayıdır')
else:
    print(f'c en büyük sayıdır ')
