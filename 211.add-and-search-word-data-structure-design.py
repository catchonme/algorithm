#!/usr/bin/python3


class TrieNode(object):
    def __init__(self):
        self.childs = dict()
        self.isWord = False


class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for letter in word:
            child = node.childs.get(letter)
            if child is None:
                child = TrieNode()
                node.childs[letter] = child
            node = child
        node.isWord = True

    def search(self, word):
        def dfs(root, word):
            if len(word) == 0:
                return root.isWord
            elif word[0] == '.':
                for node in root.childs:
                    if dfs(root.childs[node], word[1:]):
                        return True
                return False
            else:
                node = root.childs.get(word[0])
                if node is None:
                    return False
                return dfs(node, word[1:])

        return dfs(self.root, word)


