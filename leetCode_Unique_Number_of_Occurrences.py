class Solution:
    def uniqueOccurrences(self, arr):
        from collections import Counter
        count = Counter(arr)
        occurrences = list(count.values())
        return len(occurrences) == len(set(occurrences))