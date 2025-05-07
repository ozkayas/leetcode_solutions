# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def checkIfCousinsInThisLevel(nodes:Set[int]) -> Optional[bool]:
            xInLevel = x in nodes 
            yInLevel = y in nodes

            if xInLevel and yInLevel and nodes[x] != nodes[y]:
                return True
            if xInLevel or yInLevel:
                return False
            return None



        bfsQ = deque([(root, None)]) # Holds (node,parent)

        while bfsQ:
            nodes  = dict() # nodes at this level with parent
            for _ in range(len(bfsQ)):
                n, parentOfN = bfsQ.popleft()
                nodes[n.val] = parentOfN
                if n.left:
                    bfsQ.append((n.left, n))
                if n.right:
                    bfsQ.append((n.right, n))

            currentCheck = checkIfCousinsInThisLevel(nodes)
            if currentCheck != None:
                return currentCheck

        return False
            





        