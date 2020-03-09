"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by
removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only
one element is also considered to be strictly increasing.

For sequence = [1, 3, 2, 1], the output should be false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be true
"""

# Time O(n)
def nice(arr):
    alreadyRemoved = False

    for i in range(1, len(arr)):
        if (arr[i - 1] >= arr[i]):
            if alreadyRemoved or (i > 1 and len(arr)-1 > i and  arr[i - 2] >= arr[i] and arr[i - 1] >= arr[i + 1]):
                return False
            alreadyRemoved = True

    return True

print(nice([1, 2, 1, 2]))