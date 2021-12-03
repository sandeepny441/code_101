"""
https://binarysearch.com/problems/Linked-List-Deletion
"""
import ListUtil

def solve(node, target):
    temp = node
    while temp:
        temp1 = temp.next
        while temp1 and temp1.val == target:
            temp1 = temp1.next
        temp.next = temp1
        temp = temp.next
    
    # if head node removal
    if node.val == target:
        node = node.next
    return node

# ip list : 0 -> 1 -> 1 -> 2
ip = ListUtil.init_list([0, 1, 1, 2])
res = solve(ip, 1)

ListUtil.res_check('[0,2]', str(res), ip)