class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        ret = ""
        zipped = sorted(zip(indexes, sources, targets))
        n = 0
        i = 0
        for _ in range(len(S)):
            if i > len(S)-1:
                break
            try:
                x = zipped[n][0]
            except:
                pass
            if i == x:
                print("Yes")
                src = zipped[n][1]
                end = i + len(src)
                print(S[i:end] + "|" + src)
                if S[i:end] == src:
                    print("Subbed")
                    ret += zipped[n][2]
                    print(i)
                    i = end
                    print(i)
                    print()
                else:
                    ret += S[i]
                    i += 1
                n += 1
            else:
                ret += S[i]
                i += 1
        return ret
                


S = "abcd"
indexes = [0,2]
sources = ["ab","ec"]
targets = ["eee","ffff"]
# # # Output: "eeecd"

S = "vmokgggqzp"
i = [3,5,1]
so = ["kg","ggq","mo"]
t = ["s","so","bfr"]
# "v bfr s  so  zp"
# "v mo  kg ggq zp"


s = Solution()
print("Solution: " + str(s.findReplaceString(S, i, so, t)))