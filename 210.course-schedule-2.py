#!/usr/bin/python3

import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        indegrees = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegrees[course] += 1

        count, stack = self.topologicalSort(graph, indegrees)
        return stack if count == numCourses else []

    def topologicalSort(self, graph, indegrees):
        count = 0
        queue = []
        stack = []
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)
        while queue:
            course = queue.pop()
            stack.append(course)
            count += 1
            for i in graph[course]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    queue.append(i)
        return (count, stack)


sol = Solution()
res = sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
print(res)