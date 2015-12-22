class Solution(object):
    def init(self, cs, numCourses):
        initList = []
        for i in range(0, numCourses):
            if cs[i] == 0:
                initList.append(i)
        return initList

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        cs = [0] * numCourses
        for item in prerequisites:
            cs[item[0]] += len(item) - 1

        #init
        PL = self.init(cs, numCourses)
        rst = []
        remain = numCourses

        i = 0
        while i<len(PL):
            rst.append(PL[i])
            remain -= 1
            x = PL[i]
            for item in prerequisites:
                if x in item[1:len(item)]:
                    cs[item[0]] -= 1
                    if cs[item[0]] == 0:
                        PL.append(item[0])
            i = i + 1

        if remain == 0:
            return rst
        else:
            return []



numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
so = Solution()
