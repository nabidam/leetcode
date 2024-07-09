class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        idx = 0
        k = 0

        zigzag = []
        while idx < n:
            j = 0
            this_row = ["" for _ in range(numRows)]
            print(f"start of while {idx=}")
            while j < numRows:
                if idx == n:
                    break

                print(f"{j=}, {s[idx]=}")
                this_row[j] = s[idx]
                j += 1
                idx += 1
                print(f"after straight row {idx=}")
            
            zigzag.append(this_row)
            k += 1
            
            j -= 1
            while j > 1:
                print(f"{j=}")
                if idx == n:
                    break

                j -= 1
                this_row = ["" for _ in range(numRows)]
                this_row[j] = s[idx]
                print(f"after zigzag {j=}, {s[idx]=}")
                idx += 1
                zigzag.append(this_row)
                k += 1

        output = ''
        for j in range(numRows):
            for i in range(k):
                output += zigzag[i][j]

        return output




        

solution = Solution()

s = "PAYPALISHIRING"
numRows = 4

s = "ABC"
numRows = 1

print(solution.convert(s, numRows))