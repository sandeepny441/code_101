# Given a list of numbers nums and a number k, 
# return whether any two elements from the list 
# add up to k. You may not use the same element twice.
# Note: Numbers can be negative or 0.

def sum_of_two_nums(nums, k):
	if len(nums)==0 or len(nums)==1:
		return False
	seen = set()
	for num in nums:
		if k-num in seen:
			return True
		seen.add(num)
	return False

nums = [35, 8, 18, 3, 22]
k = 12

nums = []
k = 12

nums = [-3, -4, -19]
k = -7

res = sum_of_two_nums(nums, k)
print(res)
