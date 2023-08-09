# SOLVED

class Solution:
    def alphabetBoardPath(self, target):
        ret = ""
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        m = {"a": (0,0), "b": (0,1), "c": (0,2), "d": (0,3), "e": (0,4),
             "f": (1,0), "g": (1,1), "h": (1,2), "i": (1,3), "j": (1,4), 
             "k": (2,0), "l": (2,1), "m": (2,2), "n": (2,3), "o": (2,4), 
             "p": (3,0), "q": (3,1), "r": (3,2), "s": (3,3), "t": (3,4), 
             "u": (4,0), "v": (4,1), "w": (4,2), "x": (4,3), "y": (4,4), 
             "z": (5,0)}
        pos = (0,0)
        for c in target:
            print(pos)
            loc = m[c]
            ret += self.convertPath(pos, loc)
            pos = loc
        return ret
    
    def convertPath(self, cur, nxt):
        path = ""
        if nxt[0] == 5:
            y = cur[1] - nxt[1]
            if y > 0:
                path += "L"*abs(y)
            else:
                path += "R"*abs(y)
            x = cur[0] - nxt[0]
            if x > 0:
                path += "U"*abs(x)
            else:
                path += "D"*abs(x)
            print("x=" + str(x) + ",y=" + str(y))
        else:
            x = cur[0] - nxt[0]
            if x > 0:
                path += "U"*abs(x)
            else:
                path += "D"*abs(x)
            y = cur[1] - nxt[1]
            if y > 0:
                path += "L"*abs(y)
            else:
                path += "R"*abs(y)
            print("x=" + str(x) + ",y=" + str(y))
        return path + "!"



pas = [
    # "leet",     # "DDR!UURRR!!DDD!"
    # "code",     # "RR!DDRR!UUL!R!"
    "zdz",      # "DDDDD!UUUUURRR!DDDDLLLD!"
                # "DDDDD!UUUUURRR!DDDDDLLL!"
]

s = Solution()
for p in pas:
    print("Solution: " + str(s.alphabetBoardPath(p)))