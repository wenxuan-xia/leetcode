class segmentTree(object):
    val = 0
    left_end = 0
    right_end = 0
    left = None
    right = None

class NumArray(object):
    st = segmentTree()
    num = []
    def createSegmentTree(self, node):
        if node.left_end != node.right_end:
            m = (node.left_end + node.right_end) // 2

            p = segmentTree()
            p.left_end = node.left_end
            p.right_end = m
            node.left = p
            self.createSegmentTree(p)

            q = segmentTree()
            q.left_end = m + 1
            q.right_end = node.right_end
            node.right = q
            self.createSegmentTree(q)

    def InitSegmentTree(self, node, pos, val):
        node.val += val
        m = (node.left_end + node.right_end) // 2
        if pos <= m:
            if node.left != None:
                self.InitSegmentTree(node.left, pos, val)
        else:
            if node.right != None:
                self.InitSegmentTree(node.right, pos, val)


    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.num = []
        self.st = segmentTree()

        if len(nums) == 0:
            return
        self.num = nums
        self.st.left_end = 0
        self.st.right_end = len(nums) - 1
        # print self.st.left_end, self.st.right_end
        self.createSegmentTree(self.st)
        for i in range(0, len(nums)):
            self.InitSegmentTree(self.st, i, nums[i])



    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        x = self.num[i]
        y = val - x
        self.num[i] = val
        self.InitSegmentTree(self.st, i, y)
        # print self.st.val


    def getResult(self, i, j, node):
        if i>j:
            return 0
        # print node.left_end, node.right_end, i, j
        if node.left_end==i and node.right_end==j:
            return node.val
        if node.left_end<=i and node.right_end>=j:
            return self.getResult(i, min(node.left.right_end, j), node.left) + self.getResult(max(i, node.right.left_end), j, node.right)


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.getResult(i, j, self.st)

nums = [-1]
# Your NumArray object will be instantiated and called as such:
numArray = NumArray(nums)
# numArray.update(4, 6)
# numArray.update(0, 2)
# numArray.update(0, 9)
print numArray.sumRange(0, 0)
numArray.update(0, 1)
print numArray.sumRange(0, 0)
