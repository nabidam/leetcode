class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        # for input s = ""
        if not n:
            return 0
        
        longest_substr = [s[0]]
        for i in range(n):
            substr = [s[i]]
            for j in range(i + 1, n):
                substr.append(s[j])
                print(i, j, s[i], s[j], substr, longest_substr, len(set(substr)), len(substr), len(longest_substr))

                if len(set(substr)) != len(substr):
                    print("break")
                    if len(substr[:-1]) > len(longest_substr):
                        print("longest_str changed")
                        longest_substr = substr[:-1]
                    substr = substr[:-1]
                    break

            if len(substr) > len(longest_substr):
                print(substr)
                longest_substr = substr
        
        return len(longest_substr)
    


solution = Solution()

tc = "pwwkey"
tc = "pwwkew"
tc = "bbbbb"
tc = "abcabcbb"

print(solution.lengthOfLongestSubstring(tc))