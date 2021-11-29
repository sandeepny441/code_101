"""
https://binarysearch.com/problems/Unique-Ab-Strings
"""

def solve(s):
    count = 0
    for i in s:
        if i == 'a':
            count += 1
    return 2 ** count

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %s , got %s for input %s' % (expect, actual, input))

res_check(4, solve('abba'), 'abba')