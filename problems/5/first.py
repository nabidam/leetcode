class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_substr = ""
        n = len(s)

        for i in range(n):
            right_char = s[i]
            
            if n - i < len(longest_substr):
                return longest_substr
            
            for j in range(n - i):
                x = n - 1 - j
                print(i, j, x, ' => ')
                left_char = s[x]
                this_substr = s[i:x+1]
                print(right_char, left_char, this_substr, longest_substr, len(this_substr), len(longest_substr))

                if right_char == left_char and len(this_substr) > len(longest_substr):
                    len_substr = len(this_substr)
                    steps = (len_substr) // 2
                    # if not (x - i) % 2:
                    #     steps += 1

                    print(f"{steps=}")
                    flag = True
                    for k in range(steps):
                        print(f"{k=}, {len_substr - 1 - k=}, {this_substr[k]=}, {this_substr[len_substr - 1 - k]=}")
                        if this_substr[k] != this_substr[len_substr - 1 - k]:
                            flag = False
                            break
                    
                    if flag:
                        longest_substr = this_substr
                
            
        return longest_substr


        

solution = Solution()

tc1 = "babad"
tc2 = "cbbd"
tc3 = "abb"
tc4 = "abcba"
tc5 = "aacabdkacaa"

print(solution.longestPalindrome(tc5))