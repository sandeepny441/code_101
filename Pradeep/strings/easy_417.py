"""
https://binarysearch.com/problems/Longest-Common-Prefix
"""

def solve(words):
    res = []
    for items in zip(*words):
        if all(k == items[0] for k in items):
            res.append(items[0])
        else:
            break
    return ''.join(res)

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %s , got %s for input %s' % (expect, actual, input))

ip = ["anthony", "ant", "antigravity"]
res = 'ant'
res_check(res, solve(ip), ip)