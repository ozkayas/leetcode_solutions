# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        def isLeaf(node) -> bool:
            return not node.left and not node.right

        q = [(root, 1)]

        while q:
            cur = q.pop(0)
            if isLeaf(cur[0]):
                return cur[1]
            if cur[0].left:
                q.append((cur[0].left, cur[1]+1))
            if cur[0].right:
                q.append((cur[0].right, cur[1]+1))
        


    
        