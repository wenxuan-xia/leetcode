class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        f[i][j] present i-th day, status j
            i = 0..n-1
            j = 0..1    # 0: nothing in hand;  1: in hand;  2:cooldown
        f[i][j] is the maximum on i-th day with status j
        ...
        ...
        f[i+1][0] = max(f[i][0], f[i][2])
        f[i+1][1] = max(f[i][1], f[i][0]-prices[i+1])
        f[i+1][2] = max(f[i][2], f[i][1]+prices[i+1])
        """
        if len(prices) == 0:
            return 0
            
        f = []
        for i in range(0, len(prices)):
            f.append([-999999]* 3)

        f[0][0] = 0
        f[0][1] = 0 - prices[0]

        for i in range(0, len(prices) - 1):
            f[i+1][0] = max(f[i][0], f[i][2])
            f[i+1][1] = max(f[i][1], f[i][0]-prices[i+1])
            f[i+1][2] = max(f[i][2], f[i][1]+prices[i+1])

        print f
        return max(f[len(prices)-1][0], f[len(prices)-1][2])
