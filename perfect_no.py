num = int(input("Enter a number: "))
divisors = [i for i in range(1, num) if num % i == 0]

if sum(divisors) == num:
    print(f"{num} is a Perfect Number.")
else:
    print(f"{num} is not a Perfect Number.")