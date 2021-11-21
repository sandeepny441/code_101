"""
Give a list of numbers nums, 
return the number of elements 
that are in the correct indices, 
if the list were to be sorted.
"""
def solve(nums):
  nums_sorted = sorted(nums)
  res_count = 0
  for index, num in enumerate(nums):
    if nums[index] == nums_sorted[index]:
      res_count += 1
  return res_count
    

res = solve(nums = [-1, -7, 3, 4, 10])

print(res)