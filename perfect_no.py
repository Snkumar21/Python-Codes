<<<<<<< HEAD
num = int(input("Enter a number: "))
divisors = [i for i in range(1, num) if num % i == 0]

if sum(divisors) == num:
    print(f"{num} is a Perfect Number.")
else:
    print(f"{num} is not a Perfect Number.")
=======
# Example of perfect number finder in python...

num = int(input("Enter a number: "))
divisors = [i for i in range(1, num) if num % i == 0]

if sum(divisors) == num:
    print(f"{num} is a Perfect Number.")
else:
    print(f"{num} is not a Perfect Number.")
>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
