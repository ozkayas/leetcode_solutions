class Node:
    def __init__(self, key:int, value:int):
        self.prev = None
        self.next = None
        self.key = key
        self.val = value

class LRUCache:

    def __init__(self, capacity: int):
        self.hMap = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addNode(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def popNode(self, node):
        pr = node.prev
        nx = node.next
        pr.next = nx
        nx.prev =pr

    def get(self, key: int) -> int:
        if key in self.hMap:
            cur = self.hMap[key]
            self.popNode(cur)
            self.addNode(cur)
            return cur.val
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hMap:
            cur = self.hMap[key]
            cur.val = value
            self.popNode(cur)
            self.addNode(cur)
        else:
            node = Node(key, value)
            self.hMap[key] = node
            self.addNode(node)
            if len(self.hMap) > self.capacity:
                nodeToPop = self.tail.prev
                self.popNode(nodeToPop)
                del self.hMap[nodeToPop.key]

                 


        