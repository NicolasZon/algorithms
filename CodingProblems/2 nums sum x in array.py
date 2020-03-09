"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

# Time O(n)
def nice(arr, k):
    r = set()
    for i in arr:
        if i in r:
            return True
        r.add(k-i)
    return False

print(nice([10, 15, 3, 7], 17))
print(nice([10, 15, 3, 6], 17))
