# This is Fibonacci Series using user defined value.
import functools

# Value Inputter
num = int(input("Enter the number of terms: "))

# The main logic of the program
fib_series = [functools.reduce(lambda x, _: x + [x[-1] + x[-2]], range(num-2), [0, 1])][:num]

# Display the result
print("Fibonacci Series:", fib_series)
