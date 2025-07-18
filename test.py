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