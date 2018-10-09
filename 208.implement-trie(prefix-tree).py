#!/usr/bin/python3


class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.childs = dict()
        self.isWord = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            child = node.childs.get(letter)
            if child is None:
                child = TrieNode()
                node.childs[letter] = child
            node = child
        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie
        :type word: str
        :rtype: bool
        """
        node = self.root
        for i in word:
            child = node.childs.get(i)
            if child is None:
                return False
            node = child
        return node.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in thr trie
        that starts with the given prefix
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for letter in prefix:
            child = node.childs.get(letter)
            if child is None:
                return False
            node = child
        return True


trie = Trie()
trie.insert('apple')
print(trie.search("apple"))
print(trie.search('app'))
print(trie.startsWith('app'))