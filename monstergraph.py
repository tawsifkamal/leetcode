#!/bin/python3
"""
Monster Graph Pathfinding Algorithm

This module implements a pathfinding algorithm in a grid with monsters.
Finds the path from start to end that maximizes the minimum distance to monsters.

Algorithm: Modified Dijkstra's with monster distance calculation
Time Complexity: O(n*m*k + n*m*log(n*m)) where n,m are grid dimensions, k is monsters
Space Complexity: O(n*m)

Author: Leetcode Practice - HackerRank Problem
"""

import math
import os
import random
import re
import sys
import heapq



#
# Complete the 'findBestPath' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER startRow
#  4. INTEGER startColumn
#  5. INTEGER endRow
#  6. INTEGER endColumn
#  7. INTEGER_ARRAY monsterRow
#  8. INTEGER_ARRAY monsterColumn
#

def findBestPath(n, m, startRow, startColumn, endRow, endColumn, monsterRow, monsterColumn):
    # Write your code here
    # find monster coordinates
    # bfs to assign weights (for each monster)
    # run djikstras
    graph = [[-1 for _ in range(m)] for _ in range(n)]

 
    
    def dfs(r, c, cm_row, cm_col):
        if r < 0 or r >= n or c < 0 or c >= m or (r, c) in vs:
            return
            
        vs.add((r, c))
        distance = abs(cm_row - r) + abs(cm_col - c)
        print(r, c, cm_row, cm_col)
        
        if graph[r][c] == -1:
            graph[r][c] = distance
        elif graph[r][c] >= distance:
            graph[r][c] = distance

        dfs(r + 1, c, cm_row, cm_col)
        dfs(r - 1, c, cm_row, cm_col)
        dfs(r, c + 1, cm_row, cm_col)
        dfs(r, c - 1, cm_row, cm_col)
        
       
        
    pq = []
    minMonsterDistance = [10000]
    def djikstras(r, c, currDistance):
        if (r, c) in vs:
            return (False, currDistance)
            
        if r == endRow and c == endColumn:
            return (True, currDistance)
            
        vs.add((r, c))
        directions = [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]
        
        for nextR, nextC in directions:
            if nextR >= 0 and nextR < n and nextC >= 0 and nextC < m and (nextR, nextC) not in vs:
                
                
                heapq.heappush(pq, [-(graph[nextR][nextC]), nextR, nextC])
        
        
        distanceNegated, chosenR, chosenC = heapq.heappop(pq)
    
        
        if minMonsterDistance[0] >= graph[r][c]:
            minMonsterDistance[0] = graph[r][c]
        
        
        
        res = djikstras(chosenR, chosenC, -distanceNegated)
        
        return res
                
    print(n)
    print(m)  
    for i in range(len(monsterRow)):
        vs = set()
        
        cm_row = monsterRow[i]
        cm_col = monsterColumn[i]
        
        dfs(cm_row, cm_col, cm_row, cm_col)
        
        
    vs = set()
    res = djikstras(startRow, startColumn, 0)
    return minMonsterDistance[0]
   
    
        
        
        
    
    
    
    

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    startRow = int(input().strip())

    startColumn = int(input().strip())

    endRow = int(input().strip())

    endColumn = int(input().strip())

    monsterRow_count = int(input().strip())

    monsterRow = []

    for _ in range(monsterRow_count):
        monsterRow_item = int(input().strip())
        monsterRow.append(monsterRow_item)

    monsterColumn_count = int(input().strip())

    monsterColumn = []

    for _ in range(monsterColumn_count):
        monsterColumn_item = int(input().strip())
        monsterColumn.append(monsterColumn_item)

    result = findBestPath(n, m, startRow, startColumn, endRow, endColumn, monsterRow, monsterColumn)

    fptr.write(str(result) + '\n')

    fptr.close()
