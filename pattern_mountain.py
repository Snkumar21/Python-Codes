def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="\t")
        
        if i < n:
            for _ in range(2 * (n - i) - 1):
                print("\t", end="")
            for j in range(i, 0, -1):
                print(j, end="\t")
        else:
            for j in range(i - 1, 0, -1):
                print(j, end="\t")
        
        print()

if __name__ == "__main__":
    N = int(input().strip())
    print_pattern(N)