"""
https://binarysearch.com/problems/Palindrome-Count
"""

def solve(s, k):
    l = len(set(s))
    if k % 2 != 0:
        return l ** ((k // 2) + 1)
    else:
        return l ** (k//2)

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %s , got %s for input %s' % (expect, actual, input))

res_check(4, solve('ab', 4), 4)
res_check(9, solve('abc', 4), 4)