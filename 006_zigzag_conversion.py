class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        for idx, char in enumerate(s):
            rows[abs((idx+numRows-1)%((numRows-1)*2)-(numRows-1))].append(char)
        return "".join("".join(row) for row in rows)
    
s = Solution()
assert s.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert s.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
assert s.convert("A", 1) == "A"


abs(((t+len-1)%period)-(len-1))