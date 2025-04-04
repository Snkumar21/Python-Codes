class ReverseNumber:
    def __init__(self, num):
        self.num = num

    def reverse(self):
        return int(str(self.num)[::-1])

# Example usage
num = int(input("Enter a number: "))
rev = ReverseNumber(num)
print(f"Reversed number: {rev.reverse()}")