def digit_sum(n):
    return sum(int(d) for d in str(n))

def is_boston(n):
    original_sum = digit_sum(n)
    factor_sum = 0
    temp = n
    i = 2

    # Start factorizing
    while i * i <= temp:
        while temp % i == 0:
            factor_sum += digit_sum(i)
            temp //= i
        i += 1

    # If anything left, it must be a prime > sqrt(n)
    if temp > 1:
        factor_sum += digit_sum(temp)

    # It must be a *composite* number
    return original_sum == factor_sum and n != 1 and not is_prime(n)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Input and output
n = int(input())
print(1 if is_boston(n) else 0)