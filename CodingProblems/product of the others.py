"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all
the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was
[3, 2, 1], the expected output would be [2, 3, 6].

Don't use division
"""

import random

# first approach - time O(n)
def nice(arr):

    mul = 1
    for i in arr:
        mul *= i

    newArr = []

    for i in range(len(arr)):
        newArr.append( int(mul/arr[i]) )

    return newArr

# second approach without using a global var - time O(n)
def nice2(arr):

    mul = 1
    for i in range(1, len(arr)):
        mul *= arr[i]

    newArr = [mul]

    for i in range(1, len(arr)):
        newArr.append( int(newArr[i-1] / arr[i] * arr[i-1]) )

    return newArr


# this doesn't use division - time O(n)
def nice3(arr):
    productOfLeft = [1 for _ in range(len(arr))]
    productOfRight = [1 for _ in range(len(arr))]

    for i in range(1, len(arr)):
        productOfLeft[i] = productOfLeft[i-1]*arr[i-1]

    for i in range(len(arr)-2, -1, -1):
        productOfRight[i] = productOfRight[i+1]*arr[i+1]

    for i in range(len(arr)):
        arr[i] = productOfLeft[i] * productOfRight[i]

    return arr


arr = [1, 2, 3, 4, 5]
arr = [ random.randint(1, 5) for i in range(8)]

print(arr)
print(nice(arr))
print(nice2(arr))
print(nice3(arr))

