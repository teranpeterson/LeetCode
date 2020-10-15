class Solution:
    def numDecodings(self, s: str) -> int:
        return self.recurse(s)

    def recurse(self, s: str) -> int:
        if not s:
            return 1
        single = 0
        double = 0
        if int(s[0]) > 0 and int(s[0]) < 27:
            single = self.recurse(s[1:])
        if len(s) >= 2 and int(s[0]) != 0 and int(s[:2]) > 0 and int(s[:2]) < 27:
            double = self.recurse(s[2:])
        return single + double


codes = [
    "12",   # 2
    "226",  # 3
    "0",    # 0
    "1",    # 1
    "10",   # 1
    "100",  # 0
    "326",  # 2
    "2326", # 4
    "2101", # 1
]

s = Solution()
for code in codes:
    print(s.numDecodings(code))


# 2326, 0
# 2 -> 326, 1
# 3 -> 26, 2
# 2 -> 6, 3
# 6 -> , 4
# 
