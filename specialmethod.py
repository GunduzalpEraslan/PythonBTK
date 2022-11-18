mylist = [1,2,3]

myString = "my string"

print(len(mylist))
print(len(myString))

class Movie():
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie objesi oluşturuldu.")

    def __str__(self):
        return f"{self.title} by {self.director}"

m = Movie("Film adı ","Yönetmen adı", "Filmin süresi")

print(len(mylist))

print(str(m))


