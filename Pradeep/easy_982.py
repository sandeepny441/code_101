def solve(rooms, target):
    for i in rooms:
        while i >= target:
            return i
    return -1

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %d , got %d for input %s' % (expect, actual, input))

ip = [15, 10, 30, 50, 25]
target = 20
res = res_check(30, solve(ip, target), ip)

ip = [15, 10, 30, 50, 25]
target = 51
res = res_check(-1, solve(ip, target), ip)