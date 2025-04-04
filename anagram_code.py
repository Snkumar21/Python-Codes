class AnagramChecker:
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

    def is_anagram(self):
        return sorted(self.word1.lower()) == sorted(self.word2.lower())

# Example usage
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

anagram = AnagramChecker(word1, word2)
if anagram.is_anagram():
    print(f'"{word1}" and "{word2}" are anagrams')
else:
    print(f'"{word1}" and "{word2}" are not anagrams')