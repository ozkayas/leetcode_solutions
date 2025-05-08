# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        # longest path up, calculate left+right and check
        def dfs(node) -> int:
            if not node: return 0
            leftDepth = dfs(node.left)
            rightDepth = dfs(node.right)
            self.max = max(self.max, leftDepth+rightDepth)
            return max(leftDepth,rightDepth) +1

        dfs(root)
        return self.max
        