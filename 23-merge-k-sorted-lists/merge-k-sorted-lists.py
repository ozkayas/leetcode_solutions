# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None

        minHeap = []
        heapq.heapify(minHeap)
        # fill heap with first of each linked list
        for l in lists:
            if l:
                heapq.heappush(minHeap, (l.val,id(l), l))

        dummyHead = ListNode()
        head = dummyHead

        while minHeap:
            _ , _ , node = heapq.heappop(minHeap)
            dummyHead.next = node
            dummyHead = dummyHead.next
            if node.next:
                heapq.heappush(minHeap, (node.next.val,id(node.next), node.next))

        return head.next



        