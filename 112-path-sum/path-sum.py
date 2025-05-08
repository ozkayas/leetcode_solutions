# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False

        def isLeaf(node) -> bool:
            return not node.left and not node.right

        def dfs(node, curSum) -> bool:
            if isLeaf(node) and (node.val + curSum == targetSum):
                return True
            leftPath, rightPath = None, None
            if node.left:
                leftPath = dfs(node.left, node.val + curSum)
            if node.right:
                rightPath = dfs(node.right, node.val + curSum)
            if leftPath or rightPath:
                return True
            return False

        return dfs(root, 0)


        