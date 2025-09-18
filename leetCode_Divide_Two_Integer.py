class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        if dividend == INT_MIN and divisor == 1:
            return INT_MIN

        # Determine sign of result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Work with positive values
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0

        # Subtract divisor multiples using bit shifting
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        return max(INT_MIN, min(INT_MAX, sign * quotient))