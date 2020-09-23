class Solution:
    def rankTeams(self, votes):
        ret = ""
        if not votes or len(votes) < 2:
            return votes[0]
        l = len(votes[0])
        m = {}
        for vote in votes:
            for i in range(len(vote)):
                x = vote[i]
                if x not in m:
                    m[x] = [0] * l
                m[x][i] += 1
        for k, v in sorted(m.items(), key=lambda e: (e[1], e[0]), reverse=True):
            ret += k
        return str(ret)
        

pas = [
    ["ABC","ACB","ABC","ACB","ACB"],
    # Output: "ACB"   

    ["WXYZ","XYZW"],
    # Output: "XWYZ"

    ["ZMNAGUEDSJYLBOPHRQICWFXTVK"],
    # Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"

    ["BCA","CAB","CBA","ABC","ACB","BAC"],
    # Output: "ABC"

    ["M","M","M","M"],
    # Output: "M"

    ["BCA","CAB","CBA","ABC","ACB","BAC"]
    # Output: "ABC"
]

s = Solution()
for p in pas:
    print(s.rankTeams(p))