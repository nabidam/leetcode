class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        en = len(set(s))

        # for input s = ""
        if not n:
            return 0
        
        longest_substr = s[0]
        for i in range(n):
            for j in range(i + en, i + 1, -1):
                substr = s[i:j]
                print(i, j, substr, len(substr), len(set(substr)))

                if len(set(substr)) == len(substr):
                    if len(substr) > len(longest_substr):
                        print("longest_str changed")
                        longest_substr = substr


            # if len(substr) > len(longest_substr):
            #     print(substr)
            #     longest_substr = substr
        
        return len(longest_substr)
    


solution = Solution()

tc = "pwwkey"
tc = "pwwkew"
tc = "bbbbb"
tc = "abcabcbb"

print(solution.lengthOfLongestSubstring(tc))