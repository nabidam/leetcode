class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first_idx, first_num in enumerate(nums):
            for second_idx, second_num in enumerate(nums[first_idx+1:]):
                if first_num + second_num == target:
                    return [first_idx, first_idx + 1 + second_idx]

