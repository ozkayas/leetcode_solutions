from collections import defaultdict

class Node:
    def __init__(self, key: int, val: int):
        self.val, self.key = val, key
        self.next, self.prev = None, None


class DLinkList:
    def __init__(self):
        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.nodeTable = dict()  # to reach a node in O(1)

    # Insert node at the head
    def insert(self, key: int, val: int):
        node = Node(key, val)
        self.nodeTable[key] = node
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    # Pop element from the tail
    def popLast(self) -> int:
        if self.tail.prev == self.head:
            return None  # List is empty
        last = self.tail.prev
        del self.nodeTable[last.key]
        beforeLast = last.prev
        beforeLast.next = self.tail
        self.tail.prev = beforeLast
        return last.key

    # Move to head, refreshes this key in the LRU
    def remove(self, key: int):
        if key not in self.nodeTable:
            return  # Node does not exist
        nodeToRemove = self.nodeTable[key]
        nodeToRemove.next.prev = nodeToRemove.prev
        nodeToRemove.prev.next = nodeToRemove.next
        del self.nodeTable[key]

    def moveToHead(self, key: int, val: int):
        # Remove node first if it exists
        self.remove(key)
        # Insert updated or new node at the head
        self.insert(key, val)


class LFUCache:
    def __init__(self, capacity: int):
        self.table = dict()  # will hold key: value
        self.freqTable = defaultdict(DLinkList)
        self.capacity = capacity
        self.minFreq = 0  # Tracks the minimum frequency
        self.keyFreq = dict()  # Tracks the frequency of each key

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        # Update the frequency of the key
        self.updateFrequency(key)
        return self.table[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.table:
            # Update the value
            self.table[key] = value
            # Update the frequency of the key
            self.updateFrequency(key)
        else:
            # If capacity is reached, remove the least frequently used element
            if len(self.table) >= self.capacity:
                # Remove the least frequently used key, based on LRU within the same frequency
                toRemove = self.freqTable[self.minFreq].popLast()
                if toRemove is not None:
                    del self.table[toRemove]
                    del self.keyFreq[toRemove]

            # Insert the new key-value pair
            self.table[key] = value
            self.keyFreq[key] = 1
            self.freqTable[1].insert(key, value)
            self.minFreq = 1

    def updateFrequency(self, key: int):
        freq = self.keyFreq[key]
        # Remove the node from the current frequency list
        self.freqTable[freq].remove(key)

        # Update frequency
        self.keyFreq[key] += 1
        newFreq = self.keyFreq[key]
        self.freqTable[newFreq].insert(key, self.table[key])

        # Check if the old frequency list is empty and update minFreq if necessary
        if len(self.freqTable[freq].nodeTable) == 0:
            if self.minFreq == freq:
                self.minFreq += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
