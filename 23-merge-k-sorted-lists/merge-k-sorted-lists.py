# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # need id to stop comparison between tuples and not compare node objects
        Node = namedtuple("Node", ["val","id","node"])
        # fill heap with first nodes of each list
        minHeap = []
        for ls in lists:
            if ls:
                minHeap.append(Node(ls.val, id(ls), ls))
        heapq.heapify(minHeap)

        newHead = ListNode()
        dummy = newHead
        while minHeap:
            _, __, curNode = heapq.heappop(minHeap)
            dummy.next = curNode
            dummy = dummy.next 
            if curNode.next:
                heapq.heappush(minHeap, Node(curNode.next.val, id(curNode.next),curNode.next))

        return newHead.next
        


        