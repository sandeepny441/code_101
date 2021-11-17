"""
https://binarysearch.com/problems/Consecutive-Ones
"""
def solve(nums):
    got_1 = 'not_start'
    for i in nums:
        if got_1 == 'cur_seq':
            if i == 1:
                got_1 = "cur_seq"
            else:
                got_1 = "seq_done"
        elif got_1 == 'not_start':
            if i == 1:
                got_1 = "cur_seq"
            else:
                pass
        elif got_1 == 'seq_done':
            if i == 1:
                return False
            else:
                pass
    return True

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %d , got %d for input %s' % (expect, actual, input))

ip = [0, 1, 1, 1, 2, 3]
res = solve(ip)
res_check(True, res, ip)

ip = [0, 1, 1, 1, 2, 1]
res = solve(ip)
res_check(False, res, ip)