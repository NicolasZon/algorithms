
"""
Given an array of integers and an integer k, you need to find the total number of
continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""


# O(N)
def subarray_sum(nums: list, k: int) -> int:
    memo = {0: 1}
    ans = i = 0

    for num in nums:
        i += num
        ans += memo.get(i - k, 0)
        memo[i] = memo.get(i, 0) + 1

    return ans


print(subarray_sum([1, 1, 1], 2))
print(subarray_sum([1, 1, 1, 0, 2, -4, 3, -1], 2))
print(subarray_sum([0, 1, -1, 0, -1, 1, 0], 0))
print(subarray_sum([0, 1, -1, 0, -1, 1, 0], 1))
