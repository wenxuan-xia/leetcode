class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        print citations
        total = len(citations)
        l = 0
        r = len(citations)
        while (l != r):
            m = (l+r) // 2
            h = len(citations) - m - 1
            if (citations[h] <= m):
                r = m
            else:
                l = m + 1
        return l
