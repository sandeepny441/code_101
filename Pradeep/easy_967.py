"""
https://binarysearch.com/problems/ASCII-String-to-Integer
"""

def solve_1(s):
        ints = [str(x) for x in list(range(10))]
        nums = []
        total_sum = 0
        cur_num = ''
        for i in s:
            if i.isdigit():
                cur_num += i
            else:
                if cur_num:
                    total_sum += int(cur_num)
                    cur_num = ''
        # for final char
        if cur_num:
            total_sum += int(cur_num)
        return total_sum
    
# with space O(1), add recursive sum at same time
def solve(s):
    ret = 0
    cur = 0
    for i in s:
        if i in [str(x) for x in list(range(10))]:
            cur = 10 * cur + int(i)
        else:
            # accumilate
            ret += cur
            cur = 0
    return ret + cur # last digit

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %s , got %s for input %s' % (expect, actual, input))

ip = "11aa32bbb5"
res = 48
res = res_check(res, solve(ip), ip)

ip = "abc"
res = 0
res = res_check(res, solve_1(ip), ip)