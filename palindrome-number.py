class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        l = len(s)
        for i in range(0, l):
            if s[i] != s[l-1-i]:
                return False
        return True
