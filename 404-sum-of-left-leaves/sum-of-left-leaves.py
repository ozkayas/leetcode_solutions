# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = [0]

        def isLeaf(node) -> bool:
            if not node: return False
            return not node.left and not node.right

        def dfs(root):

            if isLeaf(root.left):
                ans[0] += root.left.val
            
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

        
        dfs(root)

        return ans[0]
        