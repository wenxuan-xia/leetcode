class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        rec = 0
        rst = [0]
        total = 2**n
        while total > 0:
            total -= 1
            for i in range(0, n):
                x = 2**i
                newrec = rec^x
                if newrec not in rst:
                    rst.append(newrec)
                    rec = newrec
                    break
        return rst

so = Solution()
print so.grayCode(2)
