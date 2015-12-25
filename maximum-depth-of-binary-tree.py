# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find_max_depth(self, root, level):
        le_max = level
        if root.left != None:
            le_max = max(le_max, self.find_max_depth(root.left, level+1))

        if root.right != None:
            le_max = max(le_max, self.find_max_depth(root.right, level+1))

        return le_max


    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root != None:
            return self.find_max_depth(root, 1)
        else:
            return 0
