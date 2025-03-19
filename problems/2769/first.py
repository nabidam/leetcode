class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + (t * 2)


solution = Solution()

# tc
tc = [(4, 1), (3, 2)]


for num, t in tc:
    print(solution.theMaximumAchievableX(num=num, t=t))
