"""
https://binarysearch.com/problems/Complete-an-Arithmetic-Sequence
"""

def solve(nums):
    first = nums[0]
    last = nums[-1]
    l = len(nums) + 1 # missing one
    sum_arth = ((first + last) * l ) // 2 
    actual_sum = sum(nums)
    return sum_arth - actual_sum

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %d , got %d for input %s' % (expect, actual, input))

res_check(3,solve([1, 5, 7, 9]), [1,5, 7, 9])