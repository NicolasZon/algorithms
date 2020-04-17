"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

"""

def binarySearch(arr, x):
    pos = len(arr)
    mini = 0
    maxi = pos-1
    while(maxi >= mini):
        mid = int( mini + (maxi - mini)/2 )
        if(arr[mid] >= x):
            maxi = mid-1
            pos = mid
        else:
            mini = mid+1
    return pos
            

def searchRange(arr, k):
    begins = binarySearch(arr, k)
    ends = binarySearch(arr, k+1) - 1

    if(begins > ends):
        return [-1, -1]

    return [begins, ends]

print(searchRange([5,7,7,8,8,10],8))
print(searchRange([1,2,3,7,7,8,8,8,9,10],8))
print(searchRange([5,7,7,8,8,10],6))
