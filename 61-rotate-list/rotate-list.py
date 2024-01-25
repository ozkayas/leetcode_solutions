# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None

        # find the length of the list and also tail Node
        tail = head
        lenList = 1
        while tail.next:
            lenList += 1
            tail = tail.next
        # print("tail.value, lenList", tail.val, lenList)

        k = k % lenList
        if k == 0:
            return head

        #find newTail and newHead after cutting the list
        len1 = lenList - k -1
        newTail = head

        while len1 > 0:
            len1 -= 1
            newTail = newTail.next

        newHead = newTail.next

        #Cut the list
        newTail.next = None
        # Link oldTail to old head and return newHead
        tail.next = head
        return newHead






        