class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        temp = self
        s = '['
        while temp:
            s += str(temp.val) + ","
            temp = temp.next
        if s[-1] == ',':
            s = s[:-1]
        s += ']'
        return s

def init_list(nums):
    nodes = [LLNode(x) for x in nums]
    i = 0
    head = nodes[0]
    temp = head

    for i in nodes[1:]:
        temp.next = i
        temp = temp.next
    return head

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %s , got %s for input %s' % (expect, actual, input))
