# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def build(self, root):
        if root != None:
            if root.left != None:
                root.left.next = root.right

            if root.right != None:
                if root.next != None:
                    root.right.next = root.next.left

            if root.next != None:
                self.build(root.next)

    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        self.build(root)
        if root !=None:
            if root.left !=None:
                self.connect(root.left)
