"""

massage ="Hello There. My name is Sadık turan".split()
print(massage)

my_list =[1,2,3]
print(my_list)
my_list =["bir",2,True,5.6]
print(my_list)

list1 = ["one", "two" ,"three"]
list2 = ["four","five","six"]
print(list1)
print(list2+list1)
print(len(list1+list2))

userB = ["Pelin", 3]
userA = ["Çınar", 2 ]

users = [userB, userA]
print(users[1][1])
"""
names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]
"""
# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
names.append("Cenk")
print(names)
print("")
# 2-  "Sena" değerini listenin başına ekleyiniz.
names.insert(0,"Sena")
print(names)
print("")
# 3-  "Deniz" ismini listeden siliniz.
names.remove("Deniz")
print(names)
names.pop()
print(names)
names.pop(1)
print(names)
# names.remove('Deniz')
# names.pop()
# names.pop(1)

# 4-  "Deniz" isminin indeksi nedir ?
index = names.index("Sena")
print(index)
names.pop(index)
print(index)
# index  = names.index('Deniz')
# names.pop(index)

# 5-  "Ali" listenin bir elemanı mıdır ?
if "Ali" in names:
    print("Ali listede mevcut")
else: print("ValueError: 'Ali' is not in list")


names.append("Ali")
result =names.index("Ali")
print(result)
# result = 'Ali' in names
# result = names.index('Ali')
"""
# 6-  Liste elemanlarını ters çevirin.
nam = ["A","B","C","D","E","F","G"]
print(nam.reverse())
# names.reverse()

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
namess =['Ali','Yağmur','Hakan','Deniz']
print(namess.sort())
# names.sort()

# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.
print(years.sort())

# 9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet, Dacia"
result = str.split()
print(result)
# str = "Chevrolet,Dacia"
# result = str.split(',')

# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
min=min(years)
max= max(years)
print(min,max)
# min = min(years)
# max = max(years)
# print(min, max)

# 11- years dizisinde kaç tane 1998 değeri vardır ?
result = years.count(1998)
print(result)
# 12- years dizisinin tüm elemanlarını siliniz.
print(years.clear())

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

markalar = []

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)