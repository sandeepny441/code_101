"""
https://binarysearch.com/problems/Run-Length-Decoded-String-Iterator
"""

class RunLengthDecodedIterator:
    def __init__(self, s):
        res = ''
        l = len(s)
        self.res = s
        self.cur = 0
        self.l = len(self.res)
        self.buflen = 0
        self.bufcur = 0

    def next(self):
        if self.cur < self.l:
            buffer = ""
            i = self.cur
            cur_digit = 0
            if self.bufcur >= self.buflen:
                while True:
                    try:
                        cur_digit = 10 * cur_digit + int(self.res[i])
                    except ValueError:
                        # if we are here -> it is not digit
                        buffer = self.res[i] * cur_digit
                        cur_digit = 0
                        self.buffer = buffer
                        self.buflen = len(buffer)
                        self.bufcur = 0
                        print(self.buffer)
                        self.cur = i + 1
                        break
                    i += 1
                  # main string pointer update
            print('res - ', self.buffer[self.bufcur])
            res = self.buffer[self.bufcur]
            self.bufcur += 1
            return res

    def hasnext(self):
        return self.cur < self.l

def res_check(expect, actual, input):
    if expect != actual:
        print('error : expecting %s , got %s for input %s' % (expect, actual, input))

ip = "2c"
r1 = RunLengthDecodedIterator(ip)
print(r1.next(),
r1.next(),
r1.hasnext())