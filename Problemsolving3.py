def funcArrange(inputArr):
    evens = []
    odds = []
    for num in inputArr:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    return evens + odds   # first even then odd

def main():
    # input for inputArr
    inputArr_size = int(input())       # size input (not used directly)
    inputArr = list(map(int, input().split()))

    result = funcArrange(inputArr)
    print(" ".join([str(res) for res in result]))

if __name__ == "__main__":
    main()
