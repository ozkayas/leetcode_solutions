# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSym(a,b) -> bool:
            if not a and not b: return True
            if not a or not b: return False

            if a.val == b.val and isSym(a.left, b.right) and isSym(a.right, b.left):
                return True
            return False

        return isSym(root.left, root.right) 
        