# SOLVED

class Solution:
    def longestPalindrome(self, s):
        m = 0
        sub = ""
        self.str = s
        for i in range(len(s)):
            print()
            print("i="+str(i))
            c = s[i]
            if i < len(s) - 1:
                d = s[i+1]
            else:
                d = ""
            if c == d:
                x = self.check_pal(i - 1, i + 2, 2)
            else:
                x = 0
            y = self.check_pal(i - 1, i + 1, 1)
            print("x="+str(x))
            print("y="+str(y))
            if y >= x:
                mod = 0
                n = y
            else:
                mod = 1
                n = x
            new_sub = s[i-n+1+mod:i+n]
            if len(new_sub) > len(sub):
                sub = new_sub
        return sub
            
    def check_pal(self, i, j, l):
        if i < 0 or i > len(self.str) - 1:
            return l
        if j < 0 or j > len(self.str) - 1:
            return l
        if self.str[i] != self.str[j]:
            return l
        return self.check_pal(i - 1, j + 1, l + 1)
        




pas = [
    "abc",      # a
    "aba",      # aba
    "abbc",     # bb
    "abba",     # abba
    "babad",    # bab
    "bb",       # bb
    "bbb",      # bbb
    "bbbb",     # bbbb
    "bbbbb"     # bbbbb
]

s = Solution()
for p in pas:
    print(s.longestPalindrome(p))


# s = "xxxabcxxx"
# i = 5
# n = 1
# mod = 0
# print(s[i-n+1+mod:i+n]) # c

# s = "xxxabaxxx"
# i = 4
# n = 2
# mod = 0
# print(s[i-n+1+mod:i+n]) # aba

# s = "xxxbababxxx"
# i = 5
# n = 3
# mod = 0
# print(s[i-n+1+mod:i+n]) # babab

# s = "xxxabbcxxx"
# i = 4
# n = 2
# mod = 1
# print(s[i-n+1+mod:i+n]) # bb

# s = "xxxabbaxxx"
# i = 4
# n = 3
# mod = 1
# print(s[i-n+1+mod:i+n]) # abba

# s = "xxxbbxxx"
# i = 3
# n = 2
# mod = 1
# print(s[i-n+1+mod:i+n]) # bb

# s = "xxxbbbxxx"
# i = 4
# n = 2
# mod = 0
# print(s[i-n+1+mod:i+n]) # bbb