from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(nums)
        possibles = sorted_nums[:3]
        dist = abs(sum(possibles) - target)
        for i in range(len(sorted_nums)):
            # if sorted_nums[i] > 0:
            #     break

            # if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
            #     continue

            j = i + 1
            k = len(sorted_nums) - 1
            while j < k:
                numbers = [
                    sorted_nums[i],
                    sorted_nums[j],
                    sorted_nums[k],
                ]  # sorted removed, it's just another loop (n)
                this_sum = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]

                this_dist = abs(target - this_sum)

                if dist is None or this_dist < dist:
                    possibles = numbers
                    dist = abs(this_dist)
                    j += 1
                    k -= 1
                    while sorted_nums[j] == sorted_nums[j - 1] and j < k:
                        j += 1

                else:
                    k -= 1

        return sum(possibles)


solution = Solution()

# tc
tc = [([10, 20, 30, 40, 50, 60, 70, 80, 90], 1), ([-1, 2, 1, -4], 1), ([0, 0, 0], 1)]

# tc = [[0, 0, 0]]


for nums, target in tc:
    print(solution.threeSumClosest(nums=nums, target=target))
