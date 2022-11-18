"""
name = "Çınar"
surname = "TURAN"
print("My name is {} {}.". format(name, surname))
""""""
result = 200 / 700
print("The result is {r:10.4}".format(r=result))
"""

website = "http://www.sadikturan.com"
course = "Python Kursu : Baştan sonra python programlama rehberiniz (48 saat)"

result = " HELLO WORLD ".strip()
print(result)
result = " HELLO WORLD ".lstrip()
print(result)
result = " HELLO WORLD ".rstrip()
print(result)
result = "www.sadikturan.com".strip("w.moc")
print(result)
result = course.lower()
print(result)
result = course.upper()
print(result)
result = course.title()
print(result)
result = website.count("a")
print(result)
result = website.count("www",0,10)
print(result)
result = website.startswith("www")
print(result)
result = website.startswith("http")
print(result)
result = website.endswith("com")
print(result)
result = website.find("com")
print(result)
course = course.isalpha()
print(result)
course = "Hello".isalpha()
print(result)
course = "course".isdigit()
print(result)
result = "Contents".center(50,"*")
print(result)