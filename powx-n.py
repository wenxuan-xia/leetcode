class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0:
            x = 1/x
            n = -n
            
        if n == 0:
            return 1.0
        if n == 1:
            return x

        if (n%2 == 1):
            return self.myPow(x*x, n//2)*x
        else:
            return self.myPow(x*x, n//2)
