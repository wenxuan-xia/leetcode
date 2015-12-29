class Solution(object):
    def isInteger(self, s, pos):
        """
        rtype: int
            -1: is not int
            non-neg-int: position
        """
        while pos<len(s) and s[pos].isdigit():
            pos += 1
        return pos

    def isSign(self, s, pos):
        """
        rtype: int
            -1: is not sign
            non-neg-int: position
        """
        if s[pos] == "+":
            return 1
        if s[pos] == "-":
            return -1
        return 0

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.my_calculate(s)[0]

    def my_calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, res, sign = 0, 0, 1
        while i<len(s):
            # delete blank
            while (i<len(s) and s[i]==" "):
                i += 1
            # if blank at end, return at once
            if (i == len(s)):
                return res, i

            # process
            if (s[i] == "("):
                # print "new:", s[i+1:]
                inbrace, re_pos = self.my_calculate(s[i+1:])
                res += sign*inbrace
                # print re_pos
                i += re_pos + 1
                # print s[i]
            elif (s[i] == ")"):
                return res, i
            elif (self.isSign(s, i)):
                # print "sign", s[i]
                if s[i] == "+":
                    sign = 1
                elif s[i] == "-":
                    sign = -1
            elif (self.isInteger(s, i)):
                val = s[i:self.isInteger(s, i)]
                val = int(val)
                # print "val:", val
                res += sign*val
                i = self.isInteger(s, i) - 1
            i += 1
        return res, i

s = " (3)+1"
so = Solution()
print so.calculate(s)
