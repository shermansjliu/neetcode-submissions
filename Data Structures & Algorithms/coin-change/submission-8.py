class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)

        # dp[i] = minimum number of coins it takes to get to get to i
        # dp[0] = 0
        # dp[i] = dp[i - coins[i]] + 1

        dp[0] = 0

        for i in range(1, len(dp)):
            for c in coins:
                if i - c < 0:
                    continue
                if i - c == 0:
                    dp[c] = 1
                else:
                    if dp[i-c] != -1:
                        dp[i] = min(dp[i], dp[i-c] + 1)
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]