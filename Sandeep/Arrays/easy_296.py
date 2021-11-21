"""

You are given a list of integers nums, 
representing the number of chess matches 
each person has won. 
Return a relative ranking (0-indexed) of each person. 
If two players have won the same amount, 
their ranking should be the same.


"""
#time taker
# def check_ranks(nums):
#   temp_nums = set(nums)
#   temp_nums = sorted(temp_nums, reverse = True)
#   res_list = []
#   rank_dict = {}
#   for i in temp_nums:
#     rank_dict[i] = temp_nums.index(i)
#   for i in nums:
#     res_list.append(rank_dict[i])
#   return res_list


def check_ranks(nums):
  temp_nums = set(nums)
  temp_nums = sorted(temp_nums, reverse = True)
  res_list = []
  rank_dict = {}
  prev = temp_nums[0]
  cur_rank = 0
  rank_dict[prev] = cur_rank
  for num in temp_nums[1:]:
    if num == prev:
      rank_dict[num] = cur_rank
    else:
      cur_rank += 1
      rank_dict[num] = cur_rank
      prev = num
  rank_list = []
  for num in nums:
    rank_list.append(rank_dict[num])
  return rank_list




res = check_ranks(nums = [50, 30, 50, 90, 10])
print(res)

#pradeep
# def solve(nums):
#     if not nums:
#         return []
#     nums1 = nums[:]
#     nums1.sort(reverse=True)
#     ranks = []
#     cur_rank = 0
#     prev = nums1[0]
#     rank_map = {}
#     rank_map[prev] = 0
#     for i in nums1[1:]:
#         if i == prev:
#             rank_map[i] = cur_rank
#         else:
#             cur_rank += 1
#             rank_map[i] = cur_rank
#         prev = i
#     for i in nums:
#         ranks.append(rank_map[i])
#     return ranks


# def res_check(expect, actual, input):
#     if expect != actual:
#         print('error : expecting %s , got %s for input %s' % (expect, actual, input))
#     else:
#       print(expect, actual, input)

# ip = [50, 30, 50, 90, 10]
# res_check([1, 2, 1, 0, 3], solve(ip), ip)


  