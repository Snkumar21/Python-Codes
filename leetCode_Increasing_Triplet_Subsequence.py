class Solution:
    def increasingTriplet(self, nums):
        first = float('inf')
        second = float('inf')
        
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                # Found a number bigger than both -> triplet exists
                return True
        return False