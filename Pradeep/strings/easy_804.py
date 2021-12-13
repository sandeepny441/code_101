"""
https://binarysearch.com/problems/Stuck-Keyboard
"""

def solve(typed, target):
    t1 = len(typed)
    i = 0
    cur = ""
    for t in typed:
        if i < t1 and t == target[i]:
            i += 1 # correct typed
        elif t != cur:  # should be mis typed
            return False
        cur = t

    if i == t1:
        return True
    else:
        return False

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %s , got %s for input %s' % (expect, actual, input))

res_check(True, solve('aaabcccc', 'abc'), ('aaabcccc', 'abc'))