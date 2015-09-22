class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
    	length = len(nums)
    	i = length - 1
    	while i >= 0:
    		if nums[i] == 0:
    			j = i + 1
    			while (j < length and nums[j] != 0):
    				tmp = nums[j-1]
    				nums[j-1] = nums[j]
    				nums[j] = tmp
    				j = j + 1
    		i = i - 1
    	return nums


so = Solution()
nums = [0, 1, 0, 3, 12, 0]

print so.moveZeroes(nums)