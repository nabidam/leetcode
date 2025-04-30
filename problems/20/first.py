from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        opens = []
        count = 0

        close_map = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        while count < len(s):
            if s[count] in "([{":
                opens.append(s[count])
                count += 1
            else:
                if not len(opens):
                    return False

                if close_map[s[count]] == opens[-1]:
                    opens.pop()
                    count += 1
                else:
                    return False

        if not len(opens):
            return True
        else:
            return False


solution = Solution()

# tc
tc = ["()", "()[]{}", "(]", "([])"]

# tc = [[0, 0, 0]]


for s in tc:
    print(solution.isValid(s=s))
