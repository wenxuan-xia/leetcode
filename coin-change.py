class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        oo = 9999999
        f = [oo]*(amount+1)
        f[0] = 0
        for i in range(0, amount+1):
            for coin in coins:
                if i+coin<=amount:
                    f[i+coin] = min(f[i+coin], f[i] + 1)

        if f[amount] != oo:
            return f[amount]
        else:
            return -1

so = Solution()
coins = [1, 2, 5]
amount = 15
print so.coinChange(coins, amount)
