# WORKING

class Solution:
    def numRollsToTarget(self, d, f, target):
        ret = 0
        table = []
        for n in range(d+1):
            row = [0] * (f+1)
            table.append(row)
        self.print_table(table)
        for i in range(1, d+1):
            for j in range(1, f+1):
                print("i=" + str(i) + ",j=" + str(j))
                table[i][j] = j + table[i-1][-1]
                if table[i][j] >= target:
                    ret += 1
        self.print_table(table)
        return ret
    
    def print_table(self, table):
        for row in table:
            print(row)

d = 2
f = 6
target = 7
# Output: 6


s = Solution()
print("Solution: " + str(s.numRollsToTarget(d, f, target)))