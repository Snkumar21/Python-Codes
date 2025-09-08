class Solution(object):
    def getNoZeroIntegers(self, n):
        def noZero(x):
            return '0' not in str(x)
        
        for a in range(1, n):
            b = n - a
            if noZero(a) and noZero(b):
                return [a, b]