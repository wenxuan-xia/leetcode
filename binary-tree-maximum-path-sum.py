# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):
    oo = 999999999999  #never define oo outside, you never know someone wrote it before you
    maxPath = 0
    def myMaxPathSum(self, root):
        if root == None:
            return 0
        leftMax = max(self.myMaxPathSum(root.left), 0)
        RightMax = max(self.myMaxPathSum(root.right), 0)
        # print leftMax, RightMax
        self.maxPath = max(self.maxPath, leftMax + RightMax + root.val)
        return max(leftMax, RightMax) + root.val


    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPath = -self.oo
        self.myMaxPathSum(root)
        self.myMaxPathSum
        return self.maxPath
