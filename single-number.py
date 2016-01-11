class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rst = 0
        for i in nums:
            rst = rst^i

        return rst
