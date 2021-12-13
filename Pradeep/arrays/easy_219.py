"""
https://binarysearch.com/problems/Add-One-to-List
"""

def solve(nums):
    new_num = int(''.join(str(i) for i in nums)) + 1
    res = []
    [res.append(int(i)) for i in str(new_num)]
    return res

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %s , got %s for input %s' % (expect, actual, input))

ip = [1, 9, 1]
res_check([1, 9, 2], solve(ip), ip)

ip = [9]
res_check([1, 0], solve(ip), ip)