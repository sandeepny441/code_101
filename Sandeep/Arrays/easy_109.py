"""
Given a list of integers nums, 
replace every nums[i] with the smallest integer 
left of i. Replace nums[0] with 0.

"""

def replace_with_left_smallest(nums):
  res_list = [0, nums[0]]
  smallest_left = res_list[1]
  for i,num in enumerate(nums[1:]):
      smallest_left = min(smallest_left, num)
      res_list.append(smallest_left)
  return res_list[:-1]

res = replace_with_left_smallest(nums = [10, 5, 7, 9])
print(res)