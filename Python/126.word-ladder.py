#!/usr/bin/python3


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        def backtrack(result, trace, path, word):
            if len(trace[word]) == 0:
                result.append([word] + path)
            else:
                for prev in trace[word]:
                    backtrack(result, trace, [word] + path, prev)

        lookup = set(wordList) | set([beginWord])
        res, cur, routine = [], set([beginWord]), {word: [] for word in lookup}
        while cur and endWord not in cur:
            next_queue = set()
            for word in cur:
                lookup.remove(word)
            for word in cur:
                for i in range(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i + 1:]
                        if candidate in lookup:
                            next_queue.add(candidate)
                            routine[candidate].append(word)
            cur = next_queue

        if cur:
            backtrack(res, routine, [], endWord)
        return res


beginWord = "hit",
endWord = "cog",
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
sol = Solution()
output = sol.findLadders(beginWord, endWord, wordList)
print(output)