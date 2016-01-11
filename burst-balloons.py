class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        f = []
        for i in range(0, len(nums)):
            q = []
            for j in range(0, len(nums)):
                q.append(0)
            f.append(q)

        for i in range(0, len(nums)):
            for s in range(0, len(nums)):
                t = s + i + 1
                if t<len(nums):
                    for k in range(s+1, t):
                        f[s][t] = max(f[s][t], f[s][k]+f[k][t]+nums[s]*nums[k]*nums[t])
        return f[0][len(nums)-1]

so = Solution()
nums = [3,1,5,8]
print so.maxCoins(nums)
