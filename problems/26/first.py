from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[cnt] = nums[i]
                cnt += 1
        return cnt


solution = Solution()


# tc
tc = [[1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]


for nums in tc:
    print(solution.removeDuplicates(nums=nums))
