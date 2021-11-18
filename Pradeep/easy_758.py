"""
https://binarysearch.com/problems/Fixed-Point
"""

def solve(nums): # O(n)
    found = -1
    for i in range(len(nums)):
        if i == nums[i]:
            found = i
            break
    return found

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %d , got %d for input %s' % (expect, actual, input))

nums = [-5, -2, 0, 3, 4]
res_check(3, solve(nums), nums)