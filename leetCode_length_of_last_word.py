class Solution:
    def lengthOfLastWord(self, s):
        s = s.rstrip()  # Remove trailing spaces
        last_space = s.rfind(' ')
        return len(s) - last_space - 1