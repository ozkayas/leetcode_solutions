# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        remainingRoots = [] 
        toDeleteSet = set(to_delete)
        bfsQ = deque([root])

        while bfsQ:
            cur = bfsQ.popleft()
            if cur.left:
                bfsQ.append(cur.left)
            if cur.right:
                bfsQ.append(cur.right)

            if cur.left and cur.left.val in toDeleteSet:
                cur.left = None

            if cur.right and cur.right.val in toDeleteSet:
                cur.right = None
            
            if cur.val in toDeleteSet:
                if cur.left:
                    remainingRoots.append(cur.left)
                if cur.right:
                    remainingRoots.append(cur.right)
                
        if root.val not in toDeleteSet:
            remainingRoots.append(root)

        return remainingRoots
            
