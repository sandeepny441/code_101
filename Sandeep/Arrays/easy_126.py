"""
https://binarysearch.com/problems/First-Fit-Room
"""
def solve(nums):
    return sum(nums)-len(nums)*(len(nums)-1)/2

res = solve(nums = [1,2,3,4,4])
print(res)

