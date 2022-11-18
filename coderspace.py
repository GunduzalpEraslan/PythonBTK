#!/bin/python3

import math
import os
import random
import re
import sys


# String representation of the object for cut and paste:
#     {name} is {age} years old. BMI is {bmi}

# Value errors for cut and paste:
#     Value of age should be between 18 and 120
#     Value of height should be between 100 and 250
#     Value of weight should be greater than 20

class Person(object):
    age = int(age)
    height = float(height)
    weight = int(weight)
    bmi = float(bmi)

    def __init__(self, name, age, height, weight) -> None:
        pass

    def bmi(self) -> int:
        pass

    def __str__(self) -> str:
        pass

    bmi = (weight / (height * height)

    if (age < 18 and age > 120):
        print("Value of age should be between 18 and 120")
    elif({height} < 100 and {height} > 250):
    print(" Value of height should be between 100 and 250")
    elif ({weight} < 20):
    print("Value of weight should be greater than 20")
    else:
    print(name + " is " + age + " years old. BMI is " + bmi)
    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    result = ""
    for i in range(t):
        name, age, height, weight = input().split()
    age = int(age)
    height = float(height)
    weight = int(weight)
    try:
        person_object = Person(name, age, height, weight)
    except ValueError as e:
        result += f"{e}\n"
    except Exception as e:
        result += f"{e}: Error should be passed as ValueError\n"
    else:
        result += f"{person_object}\n"
    fptr.write(result)
    fptr.close()