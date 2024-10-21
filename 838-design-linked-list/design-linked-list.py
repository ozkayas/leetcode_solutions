class MyLinkedList:

    def __init__(self):
        self.head = self.tail = None
        self.size = 0  # Liste boyutunu takip edelim
    
    def pr(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:  # Eğer geçersiz index
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:  # Eğer liste boşsa, head ve tail aynı olur
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.tail:  # Eğer liste boşsa, başa ekle
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:  # Geçersiz index
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:  # Eğer sona ekleyeceksek
            self.addAtTail(val)
        else:
            cur = self.head
            for _ in range(index-1):  # Index'e kadar ilerle
                cur = cur.next
            new_node = Node(val)
            new_node.next = cur.next
            cur.next = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:  # Geçersiz index
            return
        if index == 0:  # Baştan silme durumu
            self.head = self.head.next
            if self.size == 1:  # Tek elemanlı liste durumunda tail'i de güncelle
                self.tail = None
        else:
            cur = self.head
            for _ in range(index-1):  # Silinecek düğümden önceki düğüme git
                cur = cur.next
            cur.next = cur.next.next
            if index == self.size - 1:  # Son eleman siliniyorsa tail'i güncelle
                self.tail = cur
        self.size -= 1
        
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
