"""
https://binarysearch.com/problems/Repeating-String
"""
def solve(s):

    def check(s, i):
        interval = i
        cur_str = s[:i]
        print('check for ', i)
        eq = True
        while i < len(s):
            new_str = s[i:i+interval]
            print(cur_str, new_str)
            if cur_str != new_str:
                eq = False
            i = i + interval
        return eq

    res = None
    for i in range(2, len(s)):
        if len(s) % i == 0:
            res = check(s, i)
            print(i, res)
            if res:
                return res
            print('-------------------')
    
    if res == None:
        if len(s) == 1:
            return False
        for i in s:
            if i == s[0]:
                res = True
            else:
                res = False
                break
    return res
def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %s , got %s for input %s' % (expect, actual, input))

ip = "dogdogdog"
res = True
#res = res_check(res, solve(ip), ip)

ip = "catdog"
res = False
res = res_check(res, solve(ip), ip)

ip = "aaa"
res = True
res = res_check(res, solve(ip), ip)

ip = "ababab"
res = True
res = res_check(res, solve(ip), ip)

ip = "a"
res = False
res = res_check(res, solve(ip), ip)

ip = "awsamawsamawsam"
res = True
res = res_check(res, solve(ip), ip)


ip = "awsawsawsawsaws"
res = True
res = res_check(res, solve(ip), ip)
