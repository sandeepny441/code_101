"""
https://binarysearch.com/problems/Sorted-Elements
"""

def solve(nums): # O(n)
    nums1 = nums[:]
    nums1.sort()
    count = 0
    for i in range(len(nums1)):
        if nums1[i] == nums[i]:
            count += 1
    return count

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %d , got %d for input %s' % (expect, actual, input))

nums = [1, 7, 3, 4, 10]
res_check(2, solve(nums), nums)