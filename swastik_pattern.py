n = int(input("Enter an odd number (n ≥ 5): "))

if n < 5 or n % 2 == 0:
    print("Please enter an odd number greater than or equal to 5.")
else:
    for i in range(n):
        for j in range(n):
            # Top half
            if i == 0:
                if j >= n // 2 or j == 0:
                    print("*", end="\t")
                else:
                    print(" ", end="\t")
            # Upper middle part
            elif i < n // 2:
                if j == 0 or j == n // 2:
                    print("*", end="\t")
                else:
                    print(" ", end="\t")
            # Middle line
            elif i == n // 2:
                print("*", end="\t")
            # Bottom half
            elif i < n - 1:
                if j == n - 1 or j == n // 2:
                    print("*", end="\t")
                else:
                    print(" ", end="\t")
            # Last line
            else:
                if j <= n // 2 or j == n - 1:
                    print("*", end="\t")
                else:
                    print(" ", end="\t")
        print()