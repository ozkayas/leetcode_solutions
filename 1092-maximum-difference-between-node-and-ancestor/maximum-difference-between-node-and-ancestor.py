# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root, mi:int, ma:int):
            
            minTillThis = min(mi, root.val)
            maxTillThis = max(ma, root.val)
            
            res[0] = max(res[0],maxTillThis-minTillThis)
            if not root.left and not root.right:return
            if root.left:
                dfs(root.left, minTillThis, maxTillThis)
            if root.right:
                dfs(root.right, minTillThis, maxTillThis)
        
        dfs(root, root.val, root.val)

        return res[0]
        