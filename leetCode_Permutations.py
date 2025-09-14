class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(path, remaining):
            # Base case: if no numbers left, add current path
            if not remaining:
                res.append(path[:])
                return
            
            for i in range(len(remaining)):
                # Choose
                path.append(remaining[i])
                # Explore with remaining numbers excluding current
                backtrack(path, remaining[:i] + remaining[i+1:])
                # Undo choice
                path.pop()
        
        backtrack([], nums)
        return res