class Solution(object):
    def find_hash(self, word):
        rst = 0
        for ch in word:
            rst += ord(ch)*ord(ch)*ord(ch)*ord(ch)
        return rst

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        my_dict = dict()
        for word in strs:
            c = self.find_hash(word)
            if my_dict.has_key(c):
                my_dict[c].append(word)
            else:
                my_dict[c] = [word]

        my_list = []
        for i in my_dict:
            # print my_dict[i]
            my_dict[i].sort()
            my_list.append(my_dict[i])
        return my_list

strs = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]
so = Solution()
print so.groupAnagrams(strs)
