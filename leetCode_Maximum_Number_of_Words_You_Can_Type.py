class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        broken = set(brokenLetters)
        words = text.split()
        count = 0

        for word in words:
            if not (set(word) & broken):  # if no broken letters in this word
                count += 1

        return count