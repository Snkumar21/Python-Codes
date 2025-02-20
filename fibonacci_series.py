import functools

num = int(input("Enter the number of terms: "))
fib_series = [functools.reduce(lambda x, _: x + [x[-1] + x[-2]], range(num-2), [0, 1])][:num]
print("Fibonacci Series:", fib_series)