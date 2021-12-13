"""
https://binarysearch.com/problems/Interleaved-String
"""

def solve(s0, s1):
    l1 = len(s0)
    l2 = len(s1)

    i = 0
    j = 0
    res = ""
    while i < l1 and j < l2:
        res += s0[i] + s1[j]
        i = i + 1
        j = j + 1

    if i != l1:
        res += s0[i:]
    if j != l2:
        res += s1[j:]
    return res

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %s , got %s for input %s' % (expect, actual, input))

res_check('axbycz', solve('abc', 'xyz'), ('abc', 'xyz'))