"""
https://binarysearch.com/problems/Odd-Number-of-Digits
"""
def solve(nums):
    count = 0
    for i in nums:
        if len(str(i)) % 2 != 0:
            count += 1
    return count

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %d , got %d for input %s' % (expect, actual, input))

ip = [1, 800, 2, 10, 3]
res = res_check(4, solve(ip), ip)