# SOLVED

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ""
        step = max(numRows * 2 - 2, 1)
        sLen = len(s)
        for n in range(numRows):
            idx = n
            while True:
                tempIdx = idx - n * 2
                if tempIdx >= sLen:
                    break
                if tempIdx >= 0 and n != 0 and n != numRows - 1:
                    res += s[tempIdx]

                if idx >= sLen:
                    break
                res += s[idx]
                idx += step
        return res


s = Solution()
print(s.convert("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDE", 7) == "AMYBLNXZCKOWADJPVBEIQUCFHRTDGSE")
print(s.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
print(s.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")
print(s.convert("A", 1) == "A")