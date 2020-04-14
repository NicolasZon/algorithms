"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
"""

def findMaxLength(nums: list) -> int:
    dictAns = {}
    dictAns[0] = 0
    x = maxAns = 0
    for i in range(len(nums)):
        x += 1 if nums[i] == 1 else -1
        if x in dictAns:
            maxAns = max(maxAns, i + 1 - dictAns[x])
        else:
            dictAns[x] = i + 1
    return maxAns

print(findMaxLength([0,0,1]))
print(findMaxLength([0,0,1,0,1,1,0,0,0,0,1]))