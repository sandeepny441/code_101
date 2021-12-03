"""
https://binarysearch.com/problems/Length-of-a-Linked-List
"""
import ListUtil

def solve(node):
    temp = node
    count = 0
    while temp:
        count += 1
        temp = temp.next
    return count

ip = ListUtil.init_list([5, 4, 3])
res = 3

actual = solve(ip)
ListUtil.res_check(res, actual, ip)