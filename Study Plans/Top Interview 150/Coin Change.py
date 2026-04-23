
from typing import List

def change(coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount+1)
    dp[0] = 0

    for idx in range(1, amount+1):
        if idx in coins:
            dp[idx] = 1
        for coin in coins:
            rem = idx - coin
            if rem >= 0:
                dp[idx] = min(dp[rem]+1, dp[idx])
    print(dp)
    return dp[amount] if dp[amount] != float('inf') else -1
    


print(change([1,2,5], 11)) # 3
print(change([2], 3)) # -1
print(change([1], 0)) # 0
