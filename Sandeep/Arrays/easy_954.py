"""

You are given a list of integers nums 
which contains at least one 1. 
Return whether all the 1s appear consecutively.

"""


def solve(nums):
    if not nums:
        return None
    for num in nums:
        if num == 1:
            this_nums = nums[nums.index(num)+1:]
            cur_num = 1
            if not this_nums:
                return True
            flag_change = 0
            for this_num in this_nums:
                if this_num == 1:
                    continue
                else:
                    for this_num_2 in this_nums[this_nums.index(this_num)+1:]:
                        if this_num_2 ==1:
                            return False
                    return True
            return True
    return False

res = solve(nums = [0, 1, 1, 1, 2, 3])
print(res)