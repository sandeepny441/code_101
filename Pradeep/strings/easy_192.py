"""
https://binarysearch.com/problems/Swap-Characters-to-Equalize-Strings
"""

def solve(s, t):
    if s == t:
        return True
        
    s1 = sorted(s + t)

    i = 0 
    while i < len(s1)-1:
        if s1[i] != s1[i+1]:
            return False
        i = i +2
    return True
    
def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %s , got %s for input %s' % (expect, actual, input))

s = "aa"
t = "bb"
res = res_check(True, solve(s, t), (s, t))