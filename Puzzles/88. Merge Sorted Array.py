# SOLVED

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

s = Solution()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
s.merge(nums1, m, nums2, n)
print(nums1 == [1,2,2,3,5,6])

nums1 = [1,2,4,5,6,0]
m = 5
nums2 = [3]
n = 1
s.merge(nums1, m, nums2, n)
print(nums1 == [1,2,3,4,5,6])

nums1 = [0]
m = 0
nums2 = [1]
n = 1
s.merge(nums1, m, nums2, n)
print(nums1 == [1])

nums1 = [1]
m = 1
nums2 = []
n = 0
s.merge(nums1, m, nums2, n)
print(nums1 == [1])

nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
s.merge(nums1, m, nums2, n)
print(nums1 == [1,2,3,4,5,6])

nums1 = [1,4,7,0,0,0,0]
m = 3
nums2 = [2,3,5,6]
n = 4
s.merge(nums1, m, nums2, n)
print(nums1 == [1,2,3,4,5,6,7])

nums1 = [1,2,4,5,6,0,0]
m = 5
nums2 = [3,7]
n = 2
s.merge(nums1, m, nums2, n)
print(nums1 == [1,2,3,4,5,6,7])

#      |     |        |
# [1,2,3,0,0,0]  [2,5,6]

#      |   |        |
# [1,2,3,0,0,6]  [2,5,6]

#      | |        |
# [1,2,3,0,5,6]  [2,5,6]

#    | |          |
# [1,2,3,3,5,6]  [2,5,6]

#    |          |
# [1,2,3,3,5,6]  [2,5,6]
