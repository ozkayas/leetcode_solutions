# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMin(self, root) -> TreeNode:
        cur = root
        while cur.left:
            cur = cur.left
        return cur

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None


        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        if key == root.val:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # find smallest on the right child tree and swap with this node, then recursively rebuild right tree
            minOnRight = self.findMin(root.right)
            root.val = minOnRight.val
            root.right = self.deleteNode(root.right, root.val)

        return root
