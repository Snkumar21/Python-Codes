class Solution:
    def compress(self, chars):
        write = 0  
        left = 0   
        
        for read in range(len(chars) + 1):
            if read == len(chars) or chars[read] != chars[left]:
                chars[write] = chars[left]
                write += 1
                count = read - left
                if count > 1:
                    for c in str(count):
                        chars[write] = c
                        write += 1
                left = read
        return write