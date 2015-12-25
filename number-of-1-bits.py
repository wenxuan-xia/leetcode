class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        rst = 0
        x = 1
        for i in range(0, 100):
            # print (n or x)
            # print (n|x)
            if (n|x)==n:
                rst += 1

            x *= 2

        return rst


so = Solution()
n = 7
print so.hammingWeight(n)
