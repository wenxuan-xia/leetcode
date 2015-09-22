class Solution(object):
    def pre_process(self, t):
        q = []
        count = []
        idx = -1
        for i in t:
            idx = idx + 1
            if t.index(i) == idx:
                q.append(i)
                count.append(0)
            else:
                count[q.index(i)] = count[q.index(i)] + 1

        return q, count

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t, q = self.pre_process(t)
        print t, q
        alpha = []
        index = []
        counter = [0] *len(t)
        zero_counter = len(t)

        i = -1
        for ch in s:
        	i = i + 1
        	if ch in t:
        		alpha.append(ch)
        		index.append(i)
        min_length = 9999999999
        min_str = ""
        head = 0
        tail = -1
        flag = 0

        while tail != len(alpha)-1:
            # extand
            while zero_counter != 0:
                tail = tail + 1
                if tail > len(alpha)-1:
                    flag = 1
                    break
                x = t.index(alpha[tail])
                if (counter[x] == q[x]):
                    zero_counter = zero_counter - 1
                counter[x] = counter[x] + 1

            if flag == 1:
                break
            # shrink
            x = t.index(alpha[head])
            while (counter[x] != q[x] + 1):
                counter[x] = counter[x] - 1
                head = head + 1
                x = t.index(alpha[head])

            if min_length > index[tail] - index[head]:
                min_length = index[tail] - index[head]
                min_str = s[index[head]:index[tail] + 1]

            print head, tail
            # break and move forward
            x = t.index(alpha[head])
            counter[x] = counter[x] - 1
            if (counter[x] == q[x]):
                zero_counter = zero_counter + 1
            head = head + 1

        return min_str


test = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print test.minWindow(s, t)

