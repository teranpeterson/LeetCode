from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ret = []
        if self.verifySequence(low):
            ret.append(low)
        x = self.nextSequence(low)
        while x <= high:
            ret.append(x)
            x = self.nextSequence(x)
        if self.verifySequence(high) and high not in ret:
            ret.append(high)
        return ret
    
    def verifySequence(self, num):
        num_str = str(num)
        prev_digit = int(num_str[0])
        length = len(num_str)
        for n in range(1, length):
            next_digit = int(num_str[n])
            if prev_digit+1 != next_digit:
                return False
            prev_digit = next_digit
        return True
    
    def nextSequence(self, num):
        ret = 0
        num_str = str(num)
        digit = int(num_str[0])
        length = len(num_str)
        if length > 10:
            return float("inf")
        if digit+length > 10:
            return self.nextSequence(1*(10**(length)))
        for n in range(length):
            ret = ret * 10 + digit
            digit += 1
        if ret <= num:
            return self.nextSequence(num+(1*(10**(length-1)))-int(num_str[1:]))
        return ret


print(Solution().sequentialDigits(100, 300))
print(Solution().sequentialDigits(1000, 13000))
print(Solution().sequentialDigits(10, 1000000000))
print(Solution().sequentialDigits(58, 155))
print(Solution().sequentialDigits(123, 123))
print(Solution().sequentialDigits(234, 2314))
print([234,345,456,567,678,789,1234])
# print(Solution().nextSequence(100000000))
# print(Solution().verifySequence(123456789))
# print(Solution().verifySequence(123446789))
