from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current, left, right):
            if left == 0 and right == 0:
                result.append(current)
                return

            if left > 0:
                backtrack(current + '(', left - 1, right)

            if right > left:
                backtrack(current + ')', left, right - 1)

        backtrack("", n, n)
        return result


solution = Solution()

# tc
tc = [3, 1]

for n in tc:
    print(solution.generateParenthesis(n=n))
