class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        n = len(nums1)
        m = len(nums2)

        merged_arr = []

        p1 = 0
        p2 = 0
        while p1 < n:
            if p2 >= m:
                merged_arr.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                merged_arr.append(nums1[p1])
                p1 += 1
            elif p2 < m:
                merged_arr.append(nums2[p2])
                p2 += 1

        while p2 < m:
            merged_arr.append(nums2[p2])
            p2 += 1

        nm = n + m
        if nm % 2:
            return merged_arr[nm // 2]
        return (merged_arr[nm // 2] + merged_arr[(nm // 2) - 1]) / 2
        return merged_arr


solution = Solution()

# tc1
l1 = [1, 3]
l2 = [2]

# tc2
# l1 = [1, 2]
# l2 = [3, 4]

print(solution.findMedianSortedArrays(l1, l2))