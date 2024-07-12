class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)

        acceptable_digits = "0123456789"
        digits = []
        is_negative = False
        negativity_check = False

        # skipping
        for i in range(n):
            len_digits = len(digits)
            # if negativity sign or whitespace seen again return 0
            if negativity_check and s[i] in '-+ ' and not len_digits:
                return 0

            # ignore whitespaces
            if s[i] == " " and not len_digits:
                continue
            
            # checking negativity
            if s[i] == '-' and not len_digits:
                is_negative = True
                negativity_check = True
                continue
            
            # checking positivity
            if s[i] == '+' and not len_digits:
                is_negative = False
                negativity_check = True
                continue

            # if not starting with digits return 0
            if s[i] not in acceptable_digits and not len_digits:
                return 0
            
            # if reaching some non-digit char, break to return number
            if s[i] not in acceptable_digits and len_digits:
                break

            digits.append(int(s[i]))

        number = 0
        len_digits = len(digits)

        for i in range(len_digits):
            number += digits[i] * (10**(len_digits - i - 1))

        output = number * -1 if is_negative else number

        if output > (2**31)-1:
            return (2**31)-1
        elif output < -2**31:
            return -2**31
        return output


        

solution = Solution()

tc1 = "42"
# tc1 = "   -042"
# tc1 = "1337c0d3"
# tc1 = "0-1"
# tc1 = "words and 987"
tc1 = "+-12"

print(solution.myAtoi(tc1))