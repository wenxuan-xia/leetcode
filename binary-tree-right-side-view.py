# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    display = []
    def preOrder(self, node, level):
        if node == None:
            return
        if len(self.display)<=level:
            self.display.append(node.val)
        else:
            self.display[level] = node.val
        self.preOrder(node.left, level+1)
        self.preOrder(node.right, level+1)

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.display = []
        self.preOrder(root, 1)
        return self.display
