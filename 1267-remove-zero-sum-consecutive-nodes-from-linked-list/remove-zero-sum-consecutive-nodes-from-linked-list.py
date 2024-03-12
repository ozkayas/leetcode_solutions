# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        pre = 0
        hMap = {0:dummy} # prefix sum & node pairs
        p = head

        #fill the hmap firstly
        while p:
            pre += p.val
            hMap[pre] = p
            p = p.next
        # print(hMap.keys())
        
        #get to back and link nodes again
        p = dummy
        pre = 0
        while p:
            pre += p.val
            p.next = hMap[pre].next
            p = p.next

        return dummy.next

