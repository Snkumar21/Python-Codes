class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Edge case: if needle is empty, return 0
        if not needle:
            return 0

        # Lengths
        n, m = len(haystack), len(needle)

        # Slide window of length m across haystack
        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i

        return -1