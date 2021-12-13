"""
https://binarysearch.com/problems/Square-of-a-List
"""
def solve(nums):
    nums = [i*i for i in nums]
    nums.sort()
    return nums