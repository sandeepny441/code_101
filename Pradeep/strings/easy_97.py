"""
https://binarysearch.com/problems/Parentheses-Grouping
"""

def solve(s):
    left = None
    right = None
    open = 0
    i = 0
    start = -1
    end = -1
    res = []
    while i < len(s):
        if s[i] == '(':
            if open == 0:
                start = i
            open += 1
            
        elif s[i] == ')':
            open -= 1
            if open == 0:
                end = i
                res.append(s[start: end+1])
        i += 1
    return res

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %s , got %s for input %s' % (expect, actual, input))

ip = "()()(()())"
res = ["()", "()", "(()())"]
res_check(res, solve(ip), ip)