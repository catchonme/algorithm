#!/usr/bin/python3


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if node is None:
            return None

        root = UndirectedGraphNode(node.label)
        createdNodes = {}
        createdNodes[root.label] = root

        stack = []
        stack.append(node)

        while stack:
            cur = stack.pop()
            if cur.label in createdNodes:
                existNode = createdNodes[cur.label]
                for neighbor in cur.neighbors:
                    if neighbor.label in createdNodes:
                        existNeighbor = createdNodes[neighbor.label]
                        existNeighbor.neightbors.append(existNeighbor)
                    else:
                        newNode = undirectedGraphNode(neighbor.label)
                        existNode.neighbors.append(newNode)
                        createdNodes[neighbor.label] = newNode
                        stack.append(neighbor)

        return root

