class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        combos = sorted(enumerate(nums), key=lambda x:x[1])
        print combos
        for i in range(0, len(combos)):
            j = i + 1
            while j<len(nums) and combos[i][1] == combos[j][1]:
                if combos[j][0] - combos[i][0] <= k:
                    return True
                j += 1
        return False


so = Solution()
nums = [1,2,3,4,5,1]
so.containsNearbyDuplicate(nums, 3)
