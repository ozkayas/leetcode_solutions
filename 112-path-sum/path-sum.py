# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False

        def isLeaf(node)->bool:
            return not node.left and not node.right

        def dfs(node, target) -> bool:
            print(node.val, target)
            if target == node.val and isLeaf(node): return True
            r = target - node.val #remainder to pass to children

            if node.left and dfs(node.left, r):
                return True
            if node.right and dfs(node.right, r):
                return True

        return dfs(root, targetSum)
        
        return False

