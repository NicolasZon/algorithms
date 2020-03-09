"""
This is an explanation
"""

# Time 0(n)
def nice(arr):

    firstIndex = 0
    maxSize = 1
    actualSize = 1

    for i in range(1, len(arr)):
        if(arr[i-1] <= arr[i]):
            actualSize += 1
        else:
            if(actualSize > maxSize):
                firstIndex = i - actualSize
                maxSize = actualSize
            actualSize = 1

    if (actualSize > maxSize):
        firstIndex = len(arr) - actualSize
        maxSize = actualSize

    return arr[firstIndex:firstIndex+maxSize]

print(nice([2,1,23,33,232,1,2,3,4,4]))
print(nice([2,1,23,33,232,1,2,4]))
print(nice([2,1]))