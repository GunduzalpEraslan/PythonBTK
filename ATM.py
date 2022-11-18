
SadikHesap = {
    'ad': 'Sadik Turan',
    'hesapno' :'12345',
     'bakiye' : 3000,
     'ekHesap' : 2000
}

AliHesap= {
    'ad': 'Ali Turan',
    'hesapno': '456789213',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap,miktar):
    print(f'Merhaba {hesap["ad"]}')

    if(hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print("Paranızı alabilrisiniz")
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] +hesap['ekHesap']
        if toplam >= miktar:
            ekHassapKullanimi = input("Ek hesap kullanılsın mı (e/h")

            if ekHassapKullanimi == 'e'or'E':
                ekHassapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekHesap'] -= ekHassapKullanilacakMiktar
                print("paranızı alabilirsiniz")
                bakiyeSorgula(hesap)
            else:
                print(f'{hesap["hesapNo"]} nolu hesabınızda {hesap["bakiye"]} bulunmaktadır')
        else:
            print("Üzgünüz hesabınızda yeterli miktarda para yok")
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f'{hesap["hesapno"]} nolu hesabınızda {hesap["bakiye"]} TL bakiye bulunmaktadır. '
          f'Ek hesap liminitiniz {hesap["ekHesap"]} TL bulunmaktadır ')

paraCek(SadikHesap,3000)
print("*************")
paraCek(SadikHesap,2000)
print("*************")
paraCek(SadikHesap,100)
paraCek(AliHesap,2000)



