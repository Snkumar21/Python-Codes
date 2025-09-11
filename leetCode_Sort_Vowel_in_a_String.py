class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set("aeiouAEIOU")
        
        # Step 1: extract vowels
        vowel_list = [ch for ch in s if ch in vowels]
        
        # Step 2: sort vowels by ASCII
        vowel_list.sort()
        
        # Step 3: replace vowels in original order
        result = []
        idx = 0
        for ch in s:
            if ch in vowels:
                result.append(vowel_list[idx])
                idx += 1
            else:
                result.append(ch)
        
        return "".join(result)