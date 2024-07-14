class Solution:
    def isPalindrome(self, x: int) -> bool:
        # negatives are False
        if x < 0:
            return False
        
        # positives
        n = x
        digits = []
        while n >= 10:
            digits.append(n % 10)

            n //= 10
        digits.append(n)

        len_digits = len(digits)
        mid = len_digits // 2

        for i in range(mid):
            if digits[i] != digits[len_digits - 1 - i]:
                return False
            
        return True



        

solution = Solution()

tc1 = 121
# tc1 = -121
# tc1 = 10

print(solution.isPalindrome(tc1))