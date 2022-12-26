import numpy as np

'''numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[5:8]

print(result)

result = numbers[0:3]

print(result)

result = numbers[3:]

print(result)

result = numbers[-1]

print(result)

result = numbers[::]

print(result)

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,100]])

result = numbers2[0]

print(result)

result = numbers2[2]

print(result)

result = numbers2[0,2]

print(result)

result = numbers2[2,2]

print(result)

result = numbers2[:,2]

print(result)

result = numbers2[:2,:2]

print(result)'''

arr1 = np.arange(0,10)
arr2 = arr1.copy()

arr2[0] = 20
print(arr1)
print(arr2)


