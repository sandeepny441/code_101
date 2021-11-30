"""
https://binarysearch.com/problems/Rookie-Mistake
"""

def solve(s):
    i = 0
    got_R = False
    left_pos = False
    right_pos = False
    while i < len(s):
        if s[i] == 'B':
            if got_R:
                left_pos = True
                break
            else:
                break
        if s[i] == 'R':
            got_R = True
        i += 1
    
    if left_pos:
        return left_pos

    i = len(s) - 1
    got_R = False
    while i >= 0:
        if s[i] == 'B':
            if got_R:
                right_pos = True
                break
            else:
                break
        if s[i] == 'R':
            got_R = True
        i -= 1
    
    return right_pos

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %s , got %s for input %s' % (expect, actual, input))

ip = "......B....R.............."
res = True
res = res_check(res, solve(ip), ip)

ip = "B......B....R..............BBBB"
res = False
res = res_check(res, solve(ip), ip)