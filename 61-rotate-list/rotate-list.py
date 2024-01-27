# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        N = 1 # length of the list

        tail = head
        while tail.next:
           N +=1
           tail = tail.next
        
        # print("N:", N, "tail:", tail.val)

        k = k % N
        if k == 0:
            return head

        #Find new tail
        steps = N - k -1
        newTail = head

        while steps > 0:
            newTail = newTail.next
            steps -= 1
        
        # print("newTail", newTail.val)

        newHead = newTail.next
        tail.next = head
        newTail.next = None

        return newHead



        


