"""

Given a list of integers nums, 
return the minimum cost of sorting the 
list in ascending or descending order. 
The cost is defined as the sum of absolute differences 
between any element's old and new value.

"""

def min_sort_cost(nums):
  nums_sorted_asc = sorted(nums)
  asc_sort_cost = 0 
  for i, j in zip(nums, nums_sorted_asc):
    asc_sort_cost += abs(i - j)

  nums_sorted_desc = sorted(nums, reverse = True)
  desc_sort_cost = 0 
  for i, j in zip(nums, nums_sorted_desc):
    desc_sort_cost += abs(i - j)

  return min(asc_sort_cost, desc_sort_cost)


print(min_sort_cost([1, 4, 3]))
