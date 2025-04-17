# Example of create a class and user defined function input a range of a number from the user and display all prime numbers

class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    # main logic of the program
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # display all prime numbers in the given range
    def display_primes(self):
        print("Prime numbers between", self.start, "and", self.end, "are:")
        for num in range(self.start, self.end + 1):
            if self.is_prime(num):
                print(num, end=" ")
        print()

# Input from the user
start = int(input("Enter the starting value of the range: "))
end = int(input("Enter the ending value of the range: "))

# Creating an object and calling the method
prime_obj = PrimeNumbers(start, end)
prime_obj.display_primes()