class Solution(object):
	def reduce(self, n, i):
		while (n%i == 0):
			n = n/i
		return n
	
	def isUgly(self, num):
		if num==0:
			return False
		n = num
		t = [2,3,5]
		for i in t:
			n = self.reduce(n, i)
		if n==1:
			return True
		else:
			return False


q = Solution()
print q.isUgly(-2147483648)