class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0, len(nums)):
            # print "--", nums[i]
            if i == 0:
                if len(nums) == 1:
                    # print 1
                    return i
                elif nums[i]>nums[i+1]:
                    # print 2
                    return i
            elif i == len(nums)-1:
                if nums[i]>nums[i-1]:
                    # print 3
                    return i
            else:
                if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                    # print 4
                    return i
so = Solution()
print so.findPeakElement([1,2,3,4,5])
