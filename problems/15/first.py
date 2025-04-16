from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        possibles = []
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    numbers = sorted([nums[i], nums[j], nums[k]])
                    if numbers[0] + numbers[1] + numbers[2] == 0 and numbers not in possibles:
                        possibles.append(numbers)

        return possibles


solution = Solution()

# tc
tc = [[-1, 0, 1, 2, -1, -4], [0, 1, 1], [0, 0, 0], [11, 3, 13, -14, 12, -13, 14, -7, -1, 14, 5, -15, -11, -15, 9, 11, -6, -11, -15, -5, -3, 5, -7, 10, 11, 11, -10, -3, -4, 8, -15, -15, -4, 6, 8, -6, 8, 7, -6, -8, 6, 6, -8, 11, -1, 8, -1, 8, 13, -1, -11, -5, -11, -
                                                    3, 12, 8, -15, -13, -10, -11, 3, 12, 11, 14, 3, 4, -15, -4, -4, -13, -5, 9, 8, 2, -3, -8, -12, 12, -14, -14, -12, 12, -12, -7, -14, 8, 8, 9, 10, 13, 13, -10, 2, 9, -10, -9, -10, 12, 2, 1, 14, 13, -13, 8, -8, 0, 7, -5, -11, 0, -12, -8, -11, -8, -8, -9, -15, -15]]


for nums in tc:
    print(solution.threeSum(nums=nums))
