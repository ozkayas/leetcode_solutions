# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        Node = namedtuple("Node", ["val","id","node"])
        minHeap = []
        for root in lists:
            if root:
                minHeap.append(Node(root.val, id(root), root))
        heapq.heapify(minHeap)

        dummy = ListNode()
        cur = dummy

        while minHeap:
            popped = heapq.heappop(minHeap)
            cur.next = popped.node
            cur = cur.next
            toPutInHeap = popped.node.next
            if toPutInHeap:
                heapq.heappush(minHeap, Node(toPutInHeap.val, id(toPutInHeap), toPutInHeap))
        
        return dummy.next
        

        