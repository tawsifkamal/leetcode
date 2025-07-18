class DDL:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def removeFront(self):
        if self.head == None:
            return None
        else:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

    def removeIndex(self, node):
        if self.head == node:
            self.removeFront()

        else:
            prevNode = node.prev
            prevNode.next = node.next

            if self.tail == node:
                self.tail = self.head


class Node:
    def __init__(self, val, nextNode=None, prevNode=None):
        self.val = val
        self.next = nextNode
        self.prev = prevNode


class LRUCache:

    # Size 2 (LRU CACHE)
    # '''

    # # NOTES
    # - least recent used is at FRONT of linkedList
    # - most recently used is at BACK of linkedList

    # leastRecentLinkedList (doubly with tail)
    # 2 -><- 1

    # sizeCache = 2

    # cache (key to value)
    # 1 -> (1, pointerToOne)
    # 2 -> (2, pointerToTwo)

    # if put and new and size < Capacity:
    #     linked.addEnd(newNode(key))
    #     cache[key] = (val, newNode(key)) # store reference

    # if put and new and size >= Capacity:
    #     key = linked.getFront()
    #     linked.RemoveFront()
    #     del cache[key]
    #     linked.addEnd(newNode(newKey))
    #     cache[newKey] = (val, newKey)

    # if put and not new:
    #     val, pointerToNode = cache[key]
    #     linked.Remove(pointerToNode) # O(1)
    #     linked.addEnd(pointerToNode) # O(1)
    #     cache[key] = (newVal, pointerToNode)

    # if get:
    #     val, pointerToNode = cache[key]
    #     linked.Remove(pointerToNode) # O(1)
    #     linked.addEnd(pointerToNode) # O(1)

    # '''

    # THIS is not possible with an array because
    # we MUST use a remove from index operation in O(1) time

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.ddl = DDL()
        self.size = 0

    # if get:
    # val, pointerToNode = cache[key]
    # linked.Remove(pointerToNode) # O(1)
    # linked.addEnd(pointerToNode) # O(1)

    def get(self, key: int) -> int:
        if self.cache.get(key):
            val, node = self.cache[key]
            self.ddl.removeIndex(node)
            self.ddl.append(node)

            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if not self.cache.get(key) and self.size < self.capacity:
            newNode = Node(key)
            self.ddl.append(newNode)
            self.cache[key] = (value, newNode)
            self.size += 1
        elif not self.cache.get(key):  # then size is MUST >= self.capacity
            leastRecentKey = self.ddl.head.val
            del self.cache[leastRecentKey]
            self.ddl.removeFront()
            newNode = Node(key)
            self.ddl.append(newNode)
            self.cache[key] = (value, newNode)
        elif self.cache.get(key):
            oldVal, node = self.cache[key]
            self.ddl.removeIndex(node)
            self.ddl.append(node)  # make is most recently used (basically)
            self.cache[key] = (value, node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

instructions = ["LRUCache", "put", "put",
                "get", "get", "put", "get", "get", "get"]


# ["LRUCache", "put", "put", "get", "get", "put", "get", "get", "get"]
# [[2], [2, 1], [3, 2], [3], [2], [4, 3], [2], [3], [4]]

results = [None,None,None,2,1,None,1,-1,3]

currRes = []
obj = LRUCache(2)
currRes.append(None)
obj.put(2, 1)
currRes.append(None)
obj.put(3, 2)
currRes.append(None)
currRes.append(obj.get(3))
currRes.append(obj.get(2))
obj.put(4, 3)
currRes.append(None)
currRes.append(obj.get(2))
currRes.append(obj.get(3))
currRes.append(obj.get(4))

print(currRes)
print(results)
