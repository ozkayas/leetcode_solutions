class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If tail, just return
        def doubleNode(node) -> int:
            if not node.next:
                newVal = node.val * 2
                node.val = newVal % 10
                return newVal // 10
            
            carry = doubleNode(node.next)
            newVal = carry + (node.val * 2)
            node.val = newVal % 10
            return newVal // 10
        
        carry = doubleNode(head)

        if carry > 0:
            newNode = ListNode(carry, head)
            return newNode

        return head



        