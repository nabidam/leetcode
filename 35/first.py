from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)

        if target < nums[0]:
            return 0

        lower = 0
        upper = len(nums) - 1
        pivot = (upper + lower) // 2
        while lower < upper:
            if target == nums[pivot]:
                return pivot

            if target >= nums[pivot]:
                lower = pivot + 1
            else:
                upper = pivot - 1

            pivot = (upper + lower) // 2

        else:
            if nums[pivot] >= target:
                return pivot
            else:
                return pivot + 1


solution = Solution()


# tc
tc = [([1, 3, 5, 6], 5), ([1, 3, 5, 6], 2), ([1, 3, 5, 6], 7), ([1], 1)]


for nums, target in tc:
    print(solution.searchInsert(nums=nums, target=target))
