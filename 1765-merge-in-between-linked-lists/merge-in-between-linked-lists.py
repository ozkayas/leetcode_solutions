# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        #find nodes a-1 and b+1
        a_prev, b_next = None, None
        p = list1
        counter = 0
        while p:
            if counter == a-1:
                a_prev = p
            if counter == b+1:
                b_next = p
                break

            counter += 1
            p = p.next

        
        #find tail of list2
        tail = list2
        while tail.next:
            tail = tail.next
        

        a_prev.next = list2
        tail.next = b_next
    
        return list1