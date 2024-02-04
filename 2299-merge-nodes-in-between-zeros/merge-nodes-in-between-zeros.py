# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() 
        newHead = dummy
        cur = head.next
        temp = 0

        while cur:      
            # print("cur.val ", cur.val, "temp ", temp)
            if cur.val == 0:
                newNode = ListNode(temp)
                dummy.next = newNode
                temp = 0
                dummy = dummy.next
            else:
                temp += cur.val
            cur = cur.next

        return newHead.next