"""
You are given a list of integers nums, 
representing a decimal number and nums[i] is between [0, 9].
For example, [1, 3, 9] represents the number 139.
Return the same list in the same representation 
except modified so that 1 is added to the number.

"""

def add_one(nums):
  str_nums = ''.join(str(i) for i in nums)
  int_nums = int(str_nums)
  new_int_nums = int_nums + 1
  new_str_nums = str(new_int_nums)
  fiinal_nums = [int(i) for i in new_str_nums]
  return fiinal_nums

res = add_one([2, 9, 9, 9])
print(res)
