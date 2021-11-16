"""
https://binarysearch.com/problems/Toeplitz-Matrix
"""

def solve(matrix):
    c = len(matrix[0])
    r = len(matrix)
    #print(r,c)
    m = 0
    n = 0
    while m < r-1:
        while n < c-1:
            j = m
            if matrix[j][n] == matrix[j+1][n+1]:
                n = n + 1
                j = j + 1
            else:
                return False
        m = m + 1
        n = 0
    return True

matrix = [
    [0, 1, 2],
    [3, 0, 1],
    [4, 3, 0],
    [5, 4, 3]
]

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %d , got %d for input %s' % (expect, actual, input))

res_check(True, solve(matrix), matrix)