class Node:

    def __init__(self, key:int, val:int):
        self.val, self.key = val, key
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hMap = {}
        self.capacity = capacity
        self.head = self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self,node:Node):
        # put it at the head
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove(self,node:Node):
        # take it out from its position in the list
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.hMap:
            return -1

        self.remove(self.hMap[key])
        self.add(self.hMap[key])
        # print(self.hMap)

        return self.hMap[key].val


    def put(self, key: int, value: int) -> None:
        if key in self.hMap:
            cur = self.hMap[key]
            cur.val = value 
            self.remove(cur)
            self.add(cur)
        else:


            if len(self.hMap) >= self.capacity:
                leastNode = self.tail.prev
                self.remove(leastNode)
                self.hMap.pop(leastNode.key)

            cur = Node(key, value)
            self.hMap[key] = cur
            self.add(cur)
            # print(self.hMap)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)