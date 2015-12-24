# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    rst = []
    def postorder(self, root):
        if root != None:
            if root.left != None:
                self.postorder(root.left)
            if root.right != None:
                self.postorder(root.right)
            if root.val != None:
                self.rst.append(root.val)

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.rst = []
        self.postorder(root)
        return self.rst
