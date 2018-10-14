#!/usr/bin/python3

import collections
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        indegrees = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegrees[course] += 1
        return self.topologicalSort(graph, indegrees) == numCourses

    def topologicalSort(self, graph, indegrees):
        count = 0
        queue = []
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)
        while queue:
            course = queue.pop()
            count += 1
            for i in graph[course]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    queue.append(i)
        return count


sol = Solution()
res = sol.canFinish(2, [[1, 0], [0, 1]])
print(res)