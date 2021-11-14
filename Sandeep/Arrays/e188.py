"""
https://binarysearch.com/problems/Odd-Number-of-Digits
"""


def solve(nums):
    odd_ints = [num for num in nums if len(str(num))%2!=0]
    return len(odd_ints)

res = solve([1,344,545,6566])
print(res)