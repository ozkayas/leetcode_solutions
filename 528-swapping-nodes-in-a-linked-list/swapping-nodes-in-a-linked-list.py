# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        arr = []
        p = head
        while p:
            arr.append(p.val)
            p = p.next
        
        arr[k-1] , arr[-k] = arr[-k] , arr[k-1]

        p = head
        for val in arr:
            p.val = val
            p = p.next
        
        return head