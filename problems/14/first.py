from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cpre = ""
        flag = True

        counter = 0
        while flag and counter < len(strs[0]):
            cpre += strs[0][counter]
            for some_str in strs:
                if not some_str.startswith(cpre):
                    flag = False
                    break
            counter += 1

        if not flag:
            cpre = cpre[:-1]

        return cpre


solution = Solution()

# tc
tc = [["flower", "flow", "flight"], ["dog", "racecar", "car"], [""], ["a"]]


for strs in tc:
    print(solution.longestCommonPrefix(strs=strs))
