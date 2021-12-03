"""
https://binarysearch.com/problems/A-Strictly-Increasing-Linked-List
"""
import ListUtil

def solve(head):
    if head:
        cur_val = head.val
    temp = head.next
    while temp:
        #print(temp.val, cur_val)
        if temp.val <= cur_val:
            return False
        cur_val = temp.val
        temp = temp.next
    return True

# Testing

# for list 1 -> 5 -> 9 -> 9
ip = [1, 5, 9, 9]
head = ListUtil.init_list(ip)
ListUtil.res_check(False, solve(head), ip)

# for list 1 -> 5 -> 8 -> 9
ip = [1, 5, 8, 9]
head = ListUtil.init_list(ip)
ListUtil.res_check(True, solve(head), ip)