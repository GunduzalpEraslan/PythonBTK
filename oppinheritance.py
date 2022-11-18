# KALITIM İNHERİTANCE : MİRAS ALMA

class Person():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print("Person Created")

    def whoami(self):
        print("I am a person")

    def eat(self):
        print("I am eating")

class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.studentNumber = number
        print("Student Created")

    def whoami(self):
        print("I am a student")


p1= Person("ALİ","YILMAZ")
s1 =Student("ÇINAR","TURAN",1231231)

print(p1.fname + " " + p1.lname)
print(s1.fname + " " + s1.lname + " "+ str(s1.studentNumber))

p1.whoami()
s1.whoami()
p1.eat()
s1.eat()