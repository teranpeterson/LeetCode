class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split("=")
        l_coef, l_val = self.parse(left)
        r_coef, r_val = self.parse(right)
        # print(str(l_coef) + "x " + str(l_val) + " | " + str(r_coef) + "x " + str(r_val))
        l_coef -= r_coef
        r_coef = 0
        # print(str(l_coef) + "x " + str(l_val) + " | " + str(r_coef) + "x " + str(r_val))
        r_val -= l_val
        l_val = 0
        # print(str(l_coef) + "x " + str(l_val) + " | " + str(r_coef) + "x " + str(r_val))
        if l_coef != 1 and l_coef != 0:
            if r_val != 0:
                r_val /= l_coef
            l_coef = 1
        r_val = int(r_val)
        # print(str(l_coef) + "x " + str(l_val) + " | " + str(r_coef) + "x " + str(r_val))
        return self.finish(l_coef, l_val, r_coef, r_val)
    
    def parse(self, eq: str) -> str:
        coef = 0
        val = 0
        ex = False
        neg = False
        updated = False
        prev_num = 0
        prev_num_str = ""
        eq += "+"
        for i in range(len(eq)):
            c = eq[i]
            if c.isdigit():
                updated = True
                prev_num_str += c
                prev_num = int(prev_num_str)
            elif c == "x":
                ex = True
            else:
                if neg:
                    prev_num = -abs(prev_num)
                if ex:
                    if updated:
                        coef += prev_num
                    else:
                        if neg:
                            coef -= 1
                        else:
                            coef += 1
                else:
                    val += prev_num
                # Reset
                ex = False
                neg = False
                updated = False
                prev_num = 0
                prev_num_str = ""
                if c == "-":
                    neg = True
            # print(str(coef) + "x " + str(val))
        return coef, val
    
    def finish(self, l_coef, l_val, r_coef, r_val):
        if l_coef == 1 and l_val == 0 and r_coef == 0:
            return "x=" + str(r_val)
        elif l_coef == 0 and l_val == 0 and r_coef == 0 and r_val == 0:
            return "Infinite solutions"
        else:
            return "No solution"

print(Solution().solveEquation("x+5-3+x=6+x-2"))
print(Solution().solveEquation("x=x"))
print(Solution().solveEquation("2x=x"))
print(Solution().solveEquation("2x+3x-6x=x+2"))
print(Solution().solveEquation("x=x+2"))
print(Solution().solveEquation("3x=33+22+11"))
print(Solution().solveEquation("x=100"))
print(Solution().solveEquation("0x=0"))


# x+5-3+x=6+x-2
# 2x 2 | 1x 4
# 1x 2 | 0x 4
# 1x 0 | 0x 2

# x=x
# 1x 0 | 1x 0
# 0x 0 | 0x 0

# 2x=x
# 2x 0 | 1x 0
# 1x 0 | 0x 0

# 2x+3x-6x=x+2
#-1x 0 | 1x 2
#-2x 0 | 0x 2
# 1x 0 | 0x-1

# x=x+2
# 1x 0 | 1x 2
# 0x 0 | 0x 2

# 3x=33+22+11
# 3x 0 | 0x 66
# 1x 0 | 0x 22

# x=100
# 1x 0 | 0x 100