"""
https://binarysearch.com/problems/Anagram-Checks
"""
def solve(s0, s1):
    if len(s0) != len(s1):
        return False
    s2 = sorted(s0 + s1)
    i = 0
    while i < (len(s2)-1):
        if s2[i] != s2[i+1]:
            return False
        i += 2
    return True

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %s , got %s for input %s' % (expect, actual, input))

s0 = "listen"
s1 = "silent"
res_check(True, solve(s0, s1), (s0, s1))

s0 = "bedroom"
s1 = "bathroom"
res_check(False, solve(s0, s1), (s0, s1))
