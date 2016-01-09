class Solution(object):
    rst = []
    def gen(self, n, p, str):
        if n>0 and p>0:
            self.gen(n-1, p+1, str + "(")
            self.gen(n, p-1, str + ")")
        elif n>0:
            self.gen(n-1, p+1, str + "(")
        elif p>0:
            self.gen(n, p-1, str + ")")
        else:
            self.rst.append(str)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.rst = []
        self.gen(n, 0, "")
        return self.rst

so = Solution()
print so.generateParenthesis(1)
