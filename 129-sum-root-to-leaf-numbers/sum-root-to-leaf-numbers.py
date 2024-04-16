# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0

        def dfs(node, val):
            curVal = val*10 + node.val

            #if this is a leaf, found a value to sum up
            if not node.left and not node.right:
                self.sum += curVal
                return

            #if children exists call them
            if node.left:
                dfs(node.left, curVal)
            if node.right:
                dfs(node.right, curVal)


        
        dfs(root,0)
        return self.sum
        