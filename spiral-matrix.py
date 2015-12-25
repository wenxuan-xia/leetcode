class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rst = []
        if len(matrix) == 0:
            return rst

        # up = bottom = left = right = 0
        up = left = -1
        bottom = len(matrix)
        right = len(matrix[0])

        y = 0
        x = -1
        num = bottom*right

        # print up, left, bottom, right

        while num >0:
            # left to right
            while x<right - 1:
                x += 1
                rst.append(matrix[y][x])
                # print x,y
                num -= 1
            up += 1

            #right up to down
            if num == 0: break
            while y< bottom - 1:
                y += 1
                rst.append(matrix[y][x])
                # print x,y
                num -= 1
            right -= 1

            #right to left
            if num == 0: break
            while x>left + 1:
                x -= 1
                rst.append(matrix[y][x])
                # print x,y
                num -= 1
            # print "1", x,y
            bottom -= 1

            #down to up
            if num == 0: break
            while y>up + 1:
                y -= 1
                rst.append(matrix[y][x])
                # print x,y
                num -= 1
            left += 1
        return rst

so = Solution()
matrix = [ [ 1, 2, 3 ], [ 4, 5, 6 ],[ 7, 8, 9 ]]
print so.spiralOrder(matrix)
