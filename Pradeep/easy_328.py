"""
https://binarysearch.com/problems/123-Number-Flip
"""

def solve(nums):
    ind = -1
    for i in range(len(nums)):
        if nums[i] == '1':
            ind = i
            break
    if ind != -1:
        nums = nums[0:ind] + '3' + nums[ind + 1: ]
    return nums

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %s , got %s for input %s' % (expect, actual, input))

res_check('323', solve('123'), '123')
res_check('333', solve('333'), '333')