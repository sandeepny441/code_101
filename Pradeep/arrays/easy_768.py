"""
https://binarysearch.com/problems/Minimize-Amplitude-After-K-Removals

Still pending one *********
"""

def solve(nums, k):
    if k == 0:
        return max(nums) - min(nums)

    nums1 = nums[:]
    nums1.sort()
    n = len(nums1)
    cur_min = None
    for i in range(n-1):
        if i == 0:
            after_rem = nums1[i+k:]
        else:
            after_rem = nums1[:i] + nums1[i+k:]
        #print(after_rem, i, k)
        cur_val = max(after_rem) - min(after_rem)
        print(after_rem, cur_val)
        if not cur_min:
            cur_min = cur_val
        elif cur_val < cur_min:
            cur_min = cur_val
    return cur_min

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %s , got %s for input %s' % (expect, actual, input))

res_check(4, solve([2, 10, 14, 12, 30], 2), [2, 10, 14, 12, 30])
res_check(12, solve([2, 10, 14, 12, 30], 1), [2, 10, 14, 12, 30])
res_check(2, solve([1, 1, 0], 1), [1, 1, 0])