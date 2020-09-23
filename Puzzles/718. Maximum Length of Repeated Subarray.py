# WORKING

class Solution:
    def findLength(self, A, B):
        int_map = []
        A_len = len(A)
        B_len = len(B)
        m = 0
        for i in range(B_len):
            x = B[i]
            int_map.append([])
            for j in range(A_len):
                y = A[j]
                if x == y:
                    int_map[i].append("y")
                    # n = 1
                    # while i+n < B_len and j+n < A_len and B[i+n] == A[j+n]:
                    #     n += 1
                    # if n > m:
                    #     m = n
                else:
                    int_map[i].append("x")
        self.print_array(int_map)
        print(m)
        return m
    
    def print_array(self, ary):
        for a in ary:
            for x in a:
                print(x + " ", end="")
            print()
        
s = Solution()
s.findLength([1,2,3,2,1],[3,2,1,4,7])

# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
#   1 2 3 2 1
# 3 x x y x x
# 2 x y x y x
# 1 y x x x y
# 4 x x x x x
# 7 x x x x x

# A: [1,8,2,4,5,6,7,9,3]
# B: [3,4,5,6,7,1]
#   1 8 2 4 5 6 7 9 3
# 3 x x x x x x x x y
# 4 x x x y x x x x x
# 5 x x x x y x x x x
# 6 x x x x x y x x x
# 7 x x x x x x y x x
# 1 y x x x x x x x x

# A: []
# B: []
#   4 5 6 1 2 3 1 2 3 4 5
# 1 x x x y x x y x x x x
# 2 x x x x y x x y x x x
# 3 x x x x x y x x y x x
# 4 y x x x x x x x x y x