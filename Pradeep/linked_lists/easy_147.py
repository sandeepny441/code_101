"""
https://binarysearch.com/problems/A-Strictly-Increasing-Linked-List
"""

import ListUtil

def solve(node):
    res = ''
    temp = node
    while temp:
        res += str(temp.val)
        temp = temp.next
    return int(res, 2)

ip = [1, 0, 0]
head = ListUtil.init_list(ip)
res = 4
ListUtil.res_check(res, solve(head), ip)

ip = [1, 1, 1, 1]
head = ListUtil.init_list(ip)
res = 15
ListUtil.res_check(res, solve(head), ip)
