'''
square =  lambda num: num ** 2

numbers =[1,3,5,9,10,4]

result = list(map(square, numbers))

print(result)

'''
'''
result=list(map(lambda num: num ** 2, numbers))
result=list(map(square, numbers))
result= square(3)
'''
check_even = lambda num: num%2==0,numbers
#def check_even(num): return num%2==0
result = check_even(numbers[2])
check_even(3)
