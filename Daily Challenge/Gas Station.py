from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        for i in range(l):
            if gas[i] >= cost[i]:
                j = i
                tank = gas[j]
                while True:
                    print("Tank: " + str(tank) + " Index: " + str(j))
                    tank -= cost[j]
                    if tank < 0:
                        break
                    j = (j + 1) % l
                    tank += gas[j]
                    if j == i:
                        return i
        return -1


gas  = [2,3,4]
cost = [3,4,3]

print(Solution().canCompleteCircuit(gas, cost))