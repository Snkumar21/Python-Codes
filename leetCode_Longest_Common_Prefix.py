class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Start with the first string as prefix
        prefix = strs[0]

        for word in strs[1:]:
            # Shrink prefix until it matches the beginning of word
            while word.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix