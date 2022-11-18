x,y,z = 2,5,10
"""
a = int(input("1. sayi: "))
b = int(input("2. sayi: "))

result = (a * b) - (x + y + z)
print(result)

"""
# 2- y' nin  x' e kalansız bölümünü hesaplayınız.
'''
result = (y)//x
print(result)
'''
'''
# 3- (x,y,z) toplamının mod 3' ü nedir ?

result = (x+y+z) % 3
print(result)
'''
'''
# 4- y' nin x. kuvvetini hesaplayınız.
res = y**x
print(res)
'''
# 5- x, *y, z = numbers işlemine göre z' nin küpü kaçtır ?
numbers = 1, 5, 7, 10, 6
x, *y ,z = numbers
print(numbers)

result = z ** 3
print(result)
