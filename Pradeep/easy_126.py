def solve(nums):
    m = {}
    for i in nums:
        if i in m:
            m[i] += i
        else:
            m[i] = 1
        
    for k,v in m.items():
        if v > 1:
            return k

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %d , got %d for input %s' % (expect, actual, input))

ip = [1, 2, 3, 1]
res = solve(ip)
res_check(1, res, ip)

