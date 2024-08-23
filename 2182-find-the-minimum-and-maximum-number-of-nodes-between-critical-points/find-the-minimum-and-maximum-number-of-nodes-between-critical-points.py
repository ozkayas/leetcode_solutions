# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # Helper method to check if critical
        def isCritical(prev: int, node: ListNode) -> bool:
            if prev < node.val > node.next.val or (prev > node.val and node.val < node.next.val):
                return True
            return False

        counter = 0
        prev = head.val
        curNode = head.next
        criticals = []

        while curNode.next:
            # check if this node is critical
            if isCritical(prev, curNode):
                criticals.append(counter)
            
            # jump to next node
            prev = curNode.val
            counter += 1
            curNode = curNode.next
        
        if len(criticals) < 2:
            return [-1,-1]
        
        maxDif = criticals[-1] - criticals[0]
        minDif = float('inf')

        for i in range(1, len(criticals)):
            minDif = min(minDif, criticals[i]-criticals[i-1])

        return [minDif, maxDif]
