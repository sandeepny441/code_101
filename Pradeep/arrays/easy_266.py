"""
https://binarysearch.com/problems/Buying-Cars
"""
def solve(prices, k):
    prices.sort()
    count = 0
    sum = 0
    for i in prices:
        sum += i
        if k >= sum:
            count += 1
        else:
            break
    return count

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %d , got %d for input %s' % (expect, actual, input))

prices = [90, 30, 20, 40, 90]
k = 95
res = res_check(3, solve(prices, k), prices)

prices = [93, 157]
k = 93
res = res_check(1, solve(prices, k), prices)