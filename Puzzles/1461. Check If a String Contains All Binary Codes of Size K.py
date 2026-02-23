# SOLVED

# Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

# Example 1:

# Input: s = "00110110", k = 2
# Output: true
# Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
# Example 2:

# Input: s = "0110", k = 1
# Output: true
# Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 
# Example 3:

# Input: s = "0110", k = 2
# Output: false
# Explanation: The binary code "00" is of length 2 and does not exist in the array.

class BruteSolution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codes = []
        n = 2**k-1
        while n >= 0:
            codes.append(f"{bin(n)[2:]:0>{k}}")
            n-=1

        substrings = set()
        lp = 0
        rp = k
        while rp < len(s)+1:
            substrings.add(s[lp:rp])
            lp += 1
            rp += 1

        for code in codes:
            if code not in substrings:
                return False
        return True

class OptimalSolution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        substrings = set()
        lp = 0
        rp = k
        while rp < len(s)+1:
            substrings.add(s[lp:rp])
            lp += 1
            rp += 1

        return len(substrings) == 2**k

s = OptimalSolution()
print(s.hasAllCodes("00110110", 2) == True)
print(s.hasAllCodes("0110", 1) == True)
print(s.hasAllCodes("0110", 2) == False)
