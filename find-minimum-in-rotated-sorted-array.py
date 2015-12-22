class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l != r:
            m = (l+r)//2
            if nums[l] > nums[r]:
                if nums[m]>nums[r]:
                    l = m + 1
                else:
                    r = m
            elif nums[l] < nums[r]:
                return nums[l]
        return nums[l]

so = Solution()
nums = [2,1]
print so.findMin(nums)
