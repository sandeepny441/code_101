# Given a list of integers sorted in ascending order nums, 
# square the elements and give the output in sorted order.


def square_them(nums):
	return [num **2 for num in nums]

res = square_them([1,2,3])
print(res)