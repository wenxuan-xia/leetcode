class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        rst = 0
        while (n//5)>0:
            rst += n//5
            n = n//5

        return rst
