class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:  # closing bracket
                top = stack.pop() if stack else '#'  # pop if possible
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)  # opening bracket
        
        return not stack  # valid if stack is empty
