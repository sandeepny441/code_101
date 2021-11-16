"""
https://binarysearch.com/problems/Leaderboard
"""

def solve(nums):
    if not nums:
        return []
    nums1 = nums[:]
    nums1.sort(reverse=True)
    ranks = []
    cur_rank = 0
    prev = nums1[0]
    rank_map = {}
    rank_map[prev] = 0
    for i in nums1[1:]:
        if i == prev:
            rank_map[i] = cur_rank
        else:
            cur_rank += 1
            rank_map[i] = cur_rank
        prev = i
    for i in nums:
        ranks.append(rank_map[i])
    return ranks


def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %s , got %s for input %s' % (expect, actual, input))

ip = [50, 30, 50, 90, 10]
res_check([1, 2, 1, 0, 3], solve(ip), ip)