class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for j in xrange(coin, amount + 1):  # Use xrange for Python 2 efficiency
                dp[j] += dp[j - coin]

        return dp[amount]
