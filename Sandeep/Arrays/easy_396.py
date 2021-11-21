"""
Given a list of integers nums, 
find all duplicate numbers 
and delete their last occurrences.
"""

from collections import Counter
def solve(self, nums):
    rev_nums = nums[::-1]
    count_dict = Counter(nums)
    count
    for num in set(nums):
        if num in count_dict and count_dict[num]> 1:
            rev_nums.remove(num)
    return rev_nums[::-1]


