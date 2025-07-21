"""
Dijkstra's Shortest Path Algorithm Implementation

This module implements Dijkstra's algorithm to find the shortest path between
source and target nodes in a weighted graph using DFS with priority queue.

Algorithm: Modified Dijkstra's with DFS traversal
Time Complexity: O((V + E) log V) where V is vertices, E is edges
Space Complexity: O(V)

Author: Leetcode Practice
"""

import heapq


def djikstra(graph, source, target):
    vs = set()
    pq = []
    path = []

    def dfs(node, currDistance):
        if node == target:
            path.append(node)
            return (True, currDistance, node)

        if node in vs:
            return (False, currDistance, node)

        vs.add(node)

        for neighbor in graph[node]:
            if neighbor[0] not in vs:
                heapq.heappush(pq, (currDistance + neighbor[1], neighbor[0]))

        distance, nextNode = heapq.heappop(pq)

        res = dfs(nextNode, distance)

        if res[0] == True:
            for neighbor in graph[node]:
                if neighbor[0] == res[2]:
                    path.append(node)

        return (res[0], res[1], node)

    res = dfs(source, 0)
    return (path, res)


graph = {"A": [("B", 5), ("C", 4)], "B": [("A", 5), ("D", 7)],
         "C": [("A", 4), ("D", 400)]}
source = "A"
target = "D"

result = djikstra(graph, source, target)

print(result)
