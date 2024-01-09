# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        r1, r2 = [], []

        def dfs(root, arr):
            if not root.left and not root.right:
                arr.append(root.val)
                return

            if root.right:
                dfs(root.right, arr)
            if root.left:
                dfs(root.left, arr)
            
        
        dfs(root1, r1)
        dfs(root2, r2)

        return r1 == r2