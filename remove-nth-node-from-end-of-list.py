# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        rst = []
        counter = 0
        while head != None:
            rst.append(head.val)
            head = head.next

        rst = rst[0: len(rst)-n] + rst[len(rst)-n+1: len(rst)]
        return rst
