"""
https://binarysearch.com/problems/Linked-List-Jumps
"""
import ListUtil

def solve(node):
    temp = node
    while temp:
        val = temp.val
        i = 0
        temp1 = temp
        while i < val and temp1:
            temp1 = temp1.next
            i += 1
        temp.next = temp1
        temp = temp.next
    return node

ip = ListUtil.init_list([2, 1, 4, 1])
res = ListUtil.init_list([2, 4])

actual = solve(ip)
print(actual)