# 1- Girilen 2 sayıdan hangisi büyüktür ?
'''
a = int(input("1 : "))
b= int(input("2 : "))

if a<b :
    print("İlk sayısı ikinci sayısından küçüktür.")
else:
    print("İkinci sayısı ilk sayısından küçüktür.")

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.

vize1 = float(input('İlk vzienin puanı : '))
vize2 = float(input('İkinci vzienin puanı : '))
final = float(input('Final  puanı : '))

result = (vize1+vize2)/2 * 0.6 +final*0.4
print(result)
print(f' not ortalamanız : {ortalama } ve dersten geçme durunmunuz )
'''
# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.

a = int(input("Bir sayı giriniz :"))
if a % 2 == 0:
    print("Bu sayı çifttir")
else:
    print("Bu sayı tektir.")

    # 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
    #    (email: email@sadikturan.com parola:abc123)

email = 'email@sadikturan.com'
password = 'abc123'

girilenEmail = input('email: ')
girilenPassword = input('parola: ')

isEmail = (email == girilenEmail.lower().strip())
isPassword = (password == girilenPassword.lower())

print(f'Email bilgisi doğrumu: {isEmail} ve Parola doğru mu: {isPassword}')