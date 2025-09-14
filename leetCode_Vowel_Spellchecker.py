class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        vowels = set("aeiou")
        
        def devowel(word):
            return "".join('*' if ch in vowels else ch for ch in word.lower())
        
        exact_words = set(wordlist)
        case_map = {}
        vowel_map = {}
        
        # Build maps
        for word in wordlist:
            lower = word.lower()
            dv = devowel(word)
            if lower not in case_map:
                case_map[lower] = word
            if dv not in vowel_map:
                vowel_map[dv] = word
        
        result = []
        for q in queries:
            if q in exact_words:  # exact match
                result.append(q)
            elif q.lower() in case_map:  # case-insensitive match
                result.append(case_map[q.lower()])
            elif devowel(q) in vowel_map:  # vowel error match
                result.append(vowel_map[devowel(q)])
            else:
                result.append("")
        
        return result