class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Just fill a list with nodes and do math
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        carry = 0
        for node in reversed(nodes):
            newVal = (node.val * 2) + carry
            node.val = newVal % 10
            carry = newVal // 10
        
        if carry > 0:
            return ListNode(carry, head)
        else:
            return head



'''        # If tail, just return
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

        return head'''



        