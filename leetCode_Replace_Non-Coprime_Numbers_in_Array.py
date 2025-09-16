try:
    from math import gcd   # Python 3
except ImportError:
    from fractions import gcd   # Python 2

class Solution(object):
    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        
        for num in nums:
            stack.append(num)
            # Keep merging while last two numbers are non-coprime
            while len(stack) > 1:
                a, b = stack[-2], stack[-1]
                g = gcd(a, b)
                if g == 1:  # coprime, stop merging
                    break
                # Replace with LCM
                lcm = (a * b) // g
                stack.pop()
                stack[-1] = lcm  # update second last element
        
        return stack