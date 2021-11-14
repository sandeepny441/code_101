# Given a list of unique integers nums sorted 
# in ascending order, return the 
# minimum i such that nums[i] == i. 
# If theres no solution, return -1.

def index_equals_value(nums):
	for index, num in enumerate(nums):
		if index == num:
			return index
	return -1

res = index_equals_value([-5, -2, 0, 3, 4])
print(res)

