class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rst = 0
        mx = 0
        for nm in nums:
            rst += nm
            mx = max(mx, rst)
            if rst < 0:
                rst = 0
        if mx == 0:
            mx = -9999999
            for nm in nums:
                mx = max(mx, nm)
        return mx
