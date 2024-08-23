# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.curSum = 0

        def dfs(node: TreeNode):
            if not node: return

            # visit right node
            if node.right:
                dfs(node.right)
                
            # Do Stuff, In order traversal
            self.curSum += node.val
            node.val = self.curSum

            # visit left node
            if node.left:
                dfs(node.left)

    
        dfs(root)

        return root
        