# class
class Person:
    # class attributes
    address = 'no information'
    # constructor (yapıcı metod)
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.year = year
        print('init metodu çalıştı.')

    # methods

    def intro(self):
        print("Hello There. I am" + self.name)
    def calculateAge(self):
        return 2019 - self.year


# object (instance)
p1 = Person(name='ali', year= 1990) 
p2 = Person(name ='yağmur', year = 1995)

# updating
p1.name = 'ahmet'
p1.address = 'kocaeli' 

# accessing object attributes
print(f'p1 :name: {p1.name} year: {p1.year} address: {p1.address}')
print(f'p2 :name: {p2.name} year: {p2.year} address: {p2.address}')
p1.intro()
p2.intro()
print(f"Yaşım : {p1.calculateAge()}")

print(f"Yaşım : {p2.calculateAge()}")


class Circle :
    pi = 3.14

    def __init__(self,yaricap=1):
        self.yaricap = yaricap

    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap
    def alan_hesapla(self):
        return self.pi*self.yaricap**2

c1 = Circle()
c2 = Circle(5)

print(f"c1 : alan = {c1.alan_hesapla()} çevre ={c1.cevre_hesapla()}")

print(f"c2 : alan = {c2.alan_hesapla()} çevre ={c2.cevre_hesapla()}")
