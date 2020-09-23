import itertools

class Solution:
    def permuteUnique(self, nums):
        st = set()
        # print(list(itertools.permutations(nums)))
        for perm in itertools.permutations(nums):
            st.add(perm)
        ret = []
        for s in st:
            ret.append(list(s))
        return ret
    
    # def permute(self, lst):
    #     perms = []
    #     i = len(lst)-1
    #     while i >= 0:
    #         new_lst = [i for i in lst]
    #         new_lst[i] = lst[i-1]
    #         new_lst[i-1] = lst[i]
    #         perms.append(new_lst)
    #         i -= 1
    #     return perms

pas = [
    [1,1,2],
    # [
    #     [1,1,2],
    #     [1,2,1],
    #     [2,1,1]
    # ]
    # [1,2,3,4],
    # [[1,2,3,4],[1,2,4,3],[1,3,2,4],[1,3,4,2],[1,4,2,3],[1,4,3,2],[2,1,3,4],[2,1,4,3],[2,3,1,4],[2,3,4,1],[2,4,1,3],[2,4,3,1],[3,1,2,4],[3,1,4,2],[3,2,1,4],[3,2,4,1],[3,4,1,2],[3,4,2,1],[4,1,2,3],[4,1,3,2],[4,2,1,3],[4,2,3,1],[4,3,1,2],[4,3,2,1]]
]

s = Solution()
for p in pas:
    print("Solution: " + str(s.permuteUnique(p)))