def nice(arr):

    first = 0
    maxSize = 1
    actualSize = 1

    for i in range(1, len(arr)):
        if(arr[i-1] <= arr[i]):
            actualSize += 1
        else:
            if(actualSize > maxSize):
                first = i -actualSize
                maxSize = actualSize
            actualSize = 1

    if (actualSize > maxSize):
        first = len(arr) - actualSize
        maxSize = actualSize

    return arr[first:first+maxSize]

arr = [2,1,23,33,232,1,2,3,4,4]
print(nice(arr))