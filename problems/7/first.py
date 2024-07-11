class Solution:
    def reverse(self, x: int) -> int:
        digits = []
        is_negative = x < 0
        n = x
        if is_negative:
            n *= -1

        while n >= 10:
            digits.append(n % 10)

            n //= 10

        digits.append(n)

        reversed_number = 0

        len_digits = len(digits)
        for i in range(len_digits):
            reversed_number += digits[i] * (10 ** (len_digits - i - 1))

        output = reversed_number if not is_negative else reversed_number * -1
        if output > (2**31)-1 or output < -2**31:
            return 0
        return output



        

solution = Solution()

tc1 = 123
tc1 = -123
tc1 = 120

print(solution.reverse(tc1))