class NumArray(object):
    q = []
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.q = nums
        for i in range(1, len(self.q)):
            self.q[i] = self.q[i] + self.q[i-1]



    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i>j:
            i, j = j, i
        if i-1>=0:
            return self.q[j] - self.q[i-1]
        else:
            return self.q[j]



nums = [-2, 0, 3, -5, 2, -1]
# Your NumArray object will be instantiated and called as such:
numArray = NumArray(nums)
print numArray.sumRange(0, 1)
print numArray.sumRange(1, 2)
print numArray.sumRange(0, 5)
print numArray.sumRange(0, 2)
print numArray.sumRange(2, 5)
