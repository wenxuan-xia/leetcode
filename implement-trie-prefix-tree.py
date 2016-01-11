class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Child = dict()


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        word = word + "$"
        node = self.root
        for i in word:
            if i not in node.Child:
                node.Child[i] = TrieNode()
                # print node.Child
                node = node.Child[i]
            else:
                node = node.Child[i]


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        word += "$"
        return self.startsWith(word)


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for i in prefix:
            if i not in node.Child:
                return False
            else:
                node = node.Child[i]
        return True

# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("somestring")
# print trie.search("somestring")
# print trie.startsWith("some")
