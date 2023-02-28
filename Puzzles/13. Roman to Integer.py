# SOLVED

class Solution:
    def romanToInt(self, s: str) -> int:
        x = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        n = 0
        i = 0
        while i < len(s):
            try:
                n += x[s[i:i+2]]
                i += 2
            except:
                n += x[s[i]]
                i += 1
        return n


s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))