import random
arraySize = 10
limitMin = 0
limitMax = 100

def createArray(size,minN,maxN):
    numbers = []
    for i in range (size):
        numbers.append(random.randint(minN,maxN))
    return numbers

array = createArray(arraySize, limitMin, limitMax)
print("Unsorted:",array)
array.sort()
print("Sorted:",array)

def testMe(array):
    for i in range (arraySize-1):
        if array[i]>array[i+1]:
            print("error at position",i)

testMe(array)
