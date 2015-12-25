class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        f[i][j]
            f[i+1][0] = max( f[i][0], f[i][1]+prices[i+1] )
            f[i+1][1] = max( f[i][1], f[i][0]-prices[i+1] )
        """
        if len(prices) == 0:
            return 0

        f = []
        for i in range(0, len(prices)):
            f.append([-999999]*3)

        # print f

        f[0][0] = 0
        f[0][1] = -prices[0]

        for i in range(0, len(prices) - 1):
            f[i+1][0] = f[i][0]
            f[i+1][1] = max( f[i][1], f[i][0]-prices[i+1] )
            f[i+1][2] = max( f[i][0], f[i][1]+prices[i+1] , f[i][2])
        print f
        s = len(prices) - 1
        return max(f[s][0], f[s][2])
