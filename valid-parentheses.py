class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        f = [" "]*100000
        i = 0
        for ch in s:
            if i==0:
                f[i] = ch
                i += 1
            else:
                if (ch=="(") or (ch=="{") or (ch=="["):
                    f[i] = ch
                    i += 1
                else:
                    if (ch == "]"):
                        if f[i-1] != "[":
                            return False

                    if (ch == "}"):
                        if f[i-1] != "{":
                            return False

                    if (ch == ")"):
                        if f[i-1] != "(":
                            return False
                    i -= 1
        if i == 0:
            return True
        else:
            return False
