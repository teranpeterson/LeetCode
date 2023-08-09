# SOLVED

class Solution:
    def camelMatch(self, queries, pattern):
        ret = []
        for query in queries:
            ret.append(self.checkMatch(query, pattern))
        return ret
    
    def checkMatch(self, query, pattern):
        for c in query:
            if c.isupper():
                try:
                    q = pattern[0]
                except IndexError:
                    return False
                if q != c:
                    return False
                pattern = pattern[1:]
            else:
                try:
                    q = pattern[0]
                except IndexError:
                    pass
                if q == c:
                    pattern = pattern[1:]
        if not pattern:
            return True
        else:
            return False

queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FB"
# Output: [true,false,true,true,false]

queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FoBa"
# Output: [true,false,true,false,false]

queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FoBaT"
# Output: [false,true,false,false,false]

s = Solution()
print("Solution: " + str(s.camelMatch(queries, pattern)))