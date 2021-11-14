"""
Problem description:
https://binarysearch.com/problems/Index-with-Equal-Left-and-Right-Sums
"""

def solve(nums):
    right_sum = sum(nums[1:])
    left_sum = 0

    if right_sum == 0:
        return 0 # special case with sum of all elements zero except first

    i = 0
    j = 1
    while j < len(nums):
        left_sum += nums[i]
        right_sum -= nums[j]

        if left_sum == right_sum:
            return i+1
        j += 1
        i += 1
    return -1

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %d , got %d for input %s' % (expect, actual, input))

ip = [2, 3, 4, 0, 5, 2, 2]
res = solve(ip)
res_check(3, res, ip)

ip = [1, -2, 2]
res = solve(ip)
res_check(0, res, ip)

ip = [0]
res = solve(ip)
res_check(0, res, ip)

ip = [-1] * 60001
res = solve(ip)
res_check(30000, res, ip)


