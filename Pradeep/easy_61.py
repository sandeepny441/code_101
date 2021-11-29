"""
https://binarysearch.com/problems/Recurring-Character
"""

def solve(s):
    m = {}
    for i in range(len(s)):
        if s[i] not in m:
            m[s[i]] = 1
        else:
            return i
    return -1

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %s , got %s for input %s' % (expect, actual, input))

ip = "abcda"
res = 4
res_check(res, solve(ip), ip)

ip = "abcde"
res = -1
res_check(res, solve(ip), ip)

ip = "aaaaa"
res = 1
res_check(res, solve(ip), ip)