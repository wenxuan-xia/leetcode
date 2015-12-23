class Solution(object):
    def bi_search_one(self, matrix, target):
        l = 0
        r = len(matrix) - 1
        while l != r:
            m = (l+r) // 2
            if target < matrix[m][0]:
                r = m
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                return m
        return l

    def bi_search_two(self, vector, target):
        l = 0
        r = len(vector) - 1
        while l != r:
            m = (l+r) // 2
            if target < vector[m]:
                r = m
            elif target > vector[m]:
                l = m + 1
            else:
                return vector[m]
        return vector[l]

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        idx = self.bi_search_one(matrix, target)
        print matrix[idx]
        fetch = self.bi_search_two(matrix[idx], target)
        print fetch
        if fetch != target:
            return False
        else:
            return True

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 20
so = Solution()
print so.searchMatrix(matrix, target)
