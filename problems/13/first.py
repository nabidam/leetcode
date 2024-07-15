class Solution:
    def romanToInt(self, s: str) -> int:
        rom2nummap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        n = len(s)
        idx = 0

        number = 0
        while idx < n:
            this_letter = s[idx]
            if idx < n - 1:
                next_letter = s[idx+1]
                if rom2nummap[next_letter] > rom2nummap[this_letter]:
                    idx += 2
                    number += rom2nummap[next_letter] - rom2nummap[this_letter]
                    continue
                
                mul = 1
                idx += 1
                while next_letter == this_letter and (idx + 1) < n:
                    next_letter = s[idx+1]
                    mul += 1
                    idx += 1

                
                number += rom2nummap[this_letter] * mul

            else:
                idx += 1
                number += rom2nummap[this_letter]

        return number
    

solution = Solution()

# tc1
s = "III"

# tc2
s = "LVIII"

# tc3
s = "MCMXCIV"

# tc4
s = "DCXXI"


print(solution.romanToInt(s))