"""
Given an array of n positive integers. We need to find the largest increasing sequence of consecutive positive integers.
"""

# Time 0(n)
def largest_increasing_subarray(arr):

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

print(largest_increasing_subarray([2, 1, 23, 33, 232, 1, 2, 3, 4, 4]))
print(largest_increasing_subarray([2, 1, 23, 33, 232, 1, 2, 4]))
print(largest_increasing_subarray([2, 1]))