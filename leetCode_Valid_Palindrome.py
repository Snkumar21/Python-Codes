class Solution:
    def isPalindrome(self, s):
        filtered_chars = [ch.lower() for ch in s if ch.isalnum()]
        return filtered_chars == filtered_chars[::-1]