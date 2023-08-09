# SOLVED

class Solution:
    def rotate(self, nums, k):
        l = len(nums)
        count = 0
        start = 0
        while count < l:
            i = start
            temp = nums[i]
            while True:
                count += 1
                j = (i + k) % l
                swap = nums[j]
                nums[j] = temp
                temp = swap
                if j == start:
                    break
                else:
                    i = j
            start += 1

s = Solution()
nums = [-1,-100,3,99]
s.rotate(nums, 3)
print(nums)
