class AllOne:

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.freq = dict() # key : Node(freqOfKey)

    def inc(self, key: str) -> None:
        # First occurrence, insert in 1 freq if exists or create 1 freq and bind to head
        if key not in self.freq:
            firstNode = self.head.next
            if firstNode != self.tail and firstNode.val == 1:
                firstNode.words.add(key)
                self.freq[key] = firstNode
            else:
                newNode = Node(1)
                newNode.words.add(key)
                newNode.next = self.head.next
                self.head.next.prev = newNode
                self.head.next = newNode
                newNode.prev = self.head
                self.freq[key] = newNode
        else:
            # Clearings
            currentNode = self.freq[key]
            currentFreq = currentNode.val
            currentNode.words.discard(key)

            # Add into next node if exists, or create a new one
            nextNode = currentNode.next
            if nextNode != self.tail and nextNode.val == currentFreq + 1: # next node is just 1 bigger value, then insert in it
                nextNode.words.add(key)
                self.freq[key] = nextNode
            else: # create a new node for this frequency
                newNode = Node(currentFreq + 1)
                newNode.words.add(key)
                newNode.next = currentNode.next
                currentNode.next.prev = newNode
                currentNode.next = newNode
                newNode.prev = currentNode
                self.freq[key] = newNode

            # remove the node if no words in it:
            if len(currentNode.words) == 0:
                currentNode.prev.next = currentNode.next
                currentNode.next.prev = currentNode.prev

    def dec(self, key: str) -> None:
        # If the key does not exist, do nothing
        if key not in self.freq:
            return

        # Clearings
        currentNode = self.freq[key]
        currentFreq = currentNode.val
        currentNode.words.discard(key)

        # If the current frequency is 1, remove the key completely from the data structure
        if currentFreq == 1:
            del self.freq[key]
        else:
            # Add into previous node if exists, or create a new one
            prevNode = currentNode.prev
            if prevNode != self.head and prevNode.val == currentFreq - 1: # previous node is just 1 less value, then insert in it
                prevNode.words.add(key)
                self.freq[key] = prevNode
            else: # create a new node for this frequency
                newNode = Node(currentFreq - 1)
                newNode.words.add(key)
                newNode.next = currentNode
                newNode.prev = currentNode.prev
                currentNode.prev.next = newNode
                currentNode.prev = newNode
                self.freq[key] = newNode

        # remove the current node if no words in it
        if len(currentNode.words) == 0:
            currentNode.prev.next = currentNode.next
            currentNode.next.prev = currentNode.prev

    def getMaxKey(self) -> str:
        lastNode = self.tail.prev
        if lastNode == self.head: return ""

        for val in lastNode.words:
            return val
        

    def getMinKey(self) -> str:        
        firstNode = self.head.next
        if firstNode == self.tail: return ""

        for val in firstNode.words:
            return val


class Node:
    def __init__(self, val:int):
        self.val = val
        self.next = None
        self.prev = None
        self.words = set()
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
