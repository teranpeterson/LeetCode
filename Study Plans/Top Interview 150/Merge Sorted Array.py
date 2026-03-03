# SOLVED

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should
# be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


# [1,2,3,4,5,6] [1,2,3]
#      ^             ^

# [1,2,3,5,6,4] [3]
#        ^   ^   ^


from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if not nums2:
            return nums1

        p1 = m-1
        p2 = n-1
        d = m+n-1
        while d >= 0:
            if p2 < 0:
                nums1[d] = nums1[p1]
                p1 -= 1
            elif p1 < 0:
                nums1[d] = nums2[p2]
                p2 -= 1
            elif nums1[p1] >= nums2[p2]:
                nums1[d] = nums1[p1]
                p1 -= 1
            elif nums1[p1] < nums2[p2]:
                nums1[d] = nums2[p2]
                p2 -= 1
            d -= 1


s = Solution()
a = [1,2,3,0,0,0]
s.merge(a, 3, [2,5,6], 3)
print(a == [1,2,2,3,5,6])

b = [1]
s.merge(b, 1, [], 0)
print(b == [1])

c = [0]
s.merge(b, 0, [1], 1)
print(b == [1])

d = [4,5,6,0,0,0]
s.merge(d, 3, [1,2,3], 3)
print(d == [1,2,3,4,5,6])

e = [4,0,0,0,0,0]
s.merge(e, 1, [1,2,3,5,6], 5)
print(e == [1,2,3,4,5,6])

f = [1,2,4,5,6,0]
s.merge(f, 5, [3], 1)
print(f == [1,2,3,4,5,6])
