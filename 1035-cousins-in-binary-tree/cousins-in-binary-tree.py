# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # node,level,parent information, when found
        xNode, yNode = None, None

        def dfs(node: Optional[TreeNode], level: int, parent: int) -> bool:
            if not node:
                return

            nonlocal xNode, yNode
            #If find any of them, no need to go deeper, because they can not be cousins,if a deeper y is found
            if node.val == x:
                xNode = (node.val, level, parent) 
                return
            if node.val == y:
                yNode = (node.val, level, parent) 
                return

            dfs(node.left, level+1, node.val)
            dfs(node.right, level+1, node.val)


        dfs(root, 0, None)
        if not xNode or not yNode:
            return False
        return xNode[1] == yNode[1] and xNode[2] != yNode[2]
        
        