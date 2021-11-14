# Given a list of integers prices 
# representing prices of cars for sale, 
# and a budget k, 
# return the maximum number of cars you can buy.

def max_cars(prices,budget):
	total_cars = 0
	prices = sorted(prices)
	for price in prices:
		if price < budget:
			total_cars += 1
			budget -= price
		else:
			return total_cars
	return total_cars
prices = [90, 30, 20, 40, 90]
budget= 95


prices = [60, 90, 55, 75]
budget = 50
res = max_cars(prices, budget)
print(res)