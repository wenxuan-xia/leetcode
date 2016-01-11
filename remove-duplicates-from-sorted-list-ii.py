# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        rst = ListNode(-124982315)
        rst.next = head

        s = rst

        while s != None:
            p = s.next
            if (p != None):
                q = p.next
                if (q != None) and (q.val == p.val):
                    while (q != None) and (q.val == p.val):
                        q = q.next
                    s.next = q
                else:
                    s = p
            else:
                s = p
        return rst.next
