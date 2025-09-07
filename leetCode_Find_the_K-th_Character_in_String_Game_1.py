class Solution:
    def kthCharacter(self, k: int) -> str:
        def find_kth(k, length):
            if length == 1:
                return 'a'
            half = length // 2
            if k <= half:
                return find_kth(k, half)
            else:
                ch = find_kth(k - half, half)
                
                return chr((ord(ch) - ord('a') + 1) % 26 + ord('a'))

        length = 1

        while length < k:
            length *= 2
        return find_kth(k, length)