"""
Task Scheduling Algorithm Implementation

This module implements a solution for task scheduling with cooldown periods.
Uses heap and queue to efficiently manage task frequencies and cooldowns.

Algorithm: Greedy approach with priority queue and cooling queue
Time Complexity: O(m log k) where m is total tasks, k is unique tasks
Space Complexity: O(k)

Author: Leetcode Practice
"""

import heapq

def leastInterval(tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    # FIRST WE GET LETTER COUNT AND ADD TO HEAP
    countDict = {}
    # O(n)
    for letter in tasks:
        countDict[letter] = countDict.get(letter, 0) + 1
    letterCountArr = countDict.values() # O(n)
    letterCountHeap = [-num for num in letterCountArr] # O(n)
    heapq.heapify(letterCountHeap) #O (n)
    
    # SECOND WE REMOVE FROM HEAP AND KEEP TRACK OF ELEMENTS THAT CAN BE USED WITH QUEUE
    t = 0
    queue = []
    while len(letterCountHeap) != 0 and len(queue) != 0:
        if len(queue) != 0 and queue[0]["timeAvailable"] == t:
            letterCount = queue.pop(0)["letterCount"]
            heapq.heappush(letterCountHeap, letterCount)
        
        if len(letterCountHeap) == 0:
            t += 1
        else:
            maxLetterCount = heapq.heappop(letterCountHeap) + 1
            t += 1 
            if maxLetterCount != 0:
                queue.append({"letterCount": maxLetterCount, "timeAvailable": t + n})
    return t


leastInterval(["A", "A", "A", "B", "B", "B"], 2)