import sys

def main() -> None:
    # ---------- Fast input ----------
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return                       # empty input edge-case

    n = data[0]
    nums = data[1:1 + n]             # read exactly n ints (ignore extras)

    # ---------- Two-pointer square & sort ----------
    res = [0] * n                    # output buffer
    left, right = 0, n - 1
    pos = n - 1                      # fill from the end

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            res[pos] = nums[left] * nums[left]
            left += 1
        else:
            res[pos] = nums[right] * nums[right]
            right -= 1
        pos -= 1

    # ---------- Output ----------
    sys.stdout.write(" ".join(map(str, res)))

if __name__ == "__main__":
    main()